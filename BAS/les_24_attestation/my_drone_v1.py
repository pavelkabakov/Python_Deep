from vpython import sphere, vector, rate, cylinder, color, compound, scene, box, label

# Константы
GRAVITY = vector(0, -9.81, 0) # Вектор силы тяжести
DT = 0.01 # Шаг времени для симуляции
TARGET_ALTITUDE = 5.0 # Целевая высота, на которой дрон должен зависнуть

# Коэффициенты PID-регулятора
KP = 20.0 # Пропорциональный коэффициент
KI = 0.5 # Интегральный коэффициент
KD = 20.0 # Дифференциальный коэффициент

class Motor:
    """Представляет один мотор дрона."""
    def __init__(self, position, axis):
        self.relative_position = position
        self.axis = axis
        self.body = cylinder(pos=position, axis=axis, radius=0.02, color=color.gray(0.5))
        self.propeller = cylinder(pos=position + axis, axis=axis, radius=0.05, color=color.blue)
        self.thrust = vector(0, 0, 0)
        self.speed = 0 # Скорость мотора от 0 до 255

    def set_speed(self, speed):
        """Устанавливает скорость мотора, которая преобразуется в тягу."""
        self.speed = max(0, min(speed, 255))
        thrust_magnitude = (self.speed / 255.0) * 20
        self.thrust = vector(0, thrust_magnitude, 0)

    def update_position(self, drone_position):
        """Обновляет позицию мотора в соответствии с позицией дрона."""
        self.body.pos = drone_position + self.relative_position
        self.propeller.pos = self.body.pos + self.axis

class Drone:
    """Представляет квадрокоптер дрона."""
    def __init__(self, initial_position):
        arm_length = 0.2
        arm_thickness = 0.02

        arm1 = vector(arm_length, 0, arm_length)
        arm2 = vector(-arm_length, 0, arm_length)
        arm3 = vector(-arm_length, 0, -arm_length)
        arm4 = vector(arm_length, 0, -arm_length)

        body_sphere = sphere(pos=vector(0, 0, 0), radius=0.05, color=color.black)

        self.visual = compound([body_sphere])
        self.visual.pos = initial_position

        self.position = initial_position
        self.velocity = vector(0, 0, 0)
        self.acceleration = vector(0, 0, 0)

        self.motors = [
            Motor(position=arm1, axis=vector(0, 0.02, 0)),
            Motor(position=arm2, axis=vector(0, 0.02, 0)),
            Motor(position=arm3, axis=vector(0, 0.02, 0)),
            Motor(position=arm4, axis=vector(0, 0.02, 0)),
        ]

        # Метка для отображения координат
        self.coord_label = label(pos=initial_position, text=self.get_coordinates_text(), xoffset=20, yoffset=20, space=30, height=10, border=4, font='sans')

        # Переменные для PID-регулятора
        self.integral_error = 0.0
        self.previous_error = 0.0

    def update_physics(self):
        total_thrust = vector(0, 0, 0)
        for motor in self.motors:
            total_thrust += motor.thrust

        net_force = total_thrust + GRAVITY
        self.acceleration = net_force

        self.velocity += self.acceleration * DT
        self.position += self.velocity * DT

        self.visual.pos = self.position

        # Обновление позиций моторов
        for motor in self.motors:
            motor.update_position(self.position)

        # Обновление метки координат
        self.coord_label.pos = self.position
        self.coord_label.text = self.get_coordinates_text()

    def set_motor_speeds(self, speeds):
        for i, speed in enumerate(speeds):
            self.motors[i].set_speed(speed)

    def get_coordinates_text(self):
        return f"x: {self.position.x:.2f}, y: {self.position.y:.2f}, z: {self.position.z:.2f}"

    def maintain_altitude(self):
        # Вычисление ошибки высоты
        altitude_error = TARGET_ALTITUDE - self.position.y

        # Интегральная составляющая
        self.integral_error += altitude_error * DT

        # Дифференциальная составляющая
        derivative_error = (altitude_error - self.previous_error) / DT

        # PID управление
        speed_adjustment = (KP * altitude_error) + (KI * self.integral_error) + (KD * derivative_error)

        # Обновление предыдущей ошибки
        self.previous_error = altitude_error

        # Установка скоростей моторов
        base_speed = 150 # Базовая скорость моторов
        new_speed = base_speed + speed_adjustment
        self.set_motor_speeds([new_speed, new_speed, new_speed, new_speed])

def main():
    scene.background = color.white

    # Создание пола
    floor = box(pos=vector(0, 0, 0), size=vector(5, 0.01, 5), color=color.green)

    drone = Drone(initial_position=vector(0, 1, 0))

    while True:
        rate(100)

        # Управление высотой
        drone.maintain_altitude()

        drone.update_physics()

if __name__ == "__main__":
    main()