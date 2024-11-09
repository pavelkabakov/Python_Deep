from vpython import *

# Создаем окно для отображения 3D-сцены
scene = canvas(title='Прыгающий мяч')

# Создаем сферу и платформу
ball = sphere(pos=vector(0, 10, 0), radius=0.5, color=color.blue)
ground = box(pos=vector(0, 0, 0), size=vector(10, 0.1, 10), color=color.green)

# Параметры симуляции
g = 9.8  # Ускорение свободного падения
ball.velocity = vector(0, 0, 0)  # Начальная скорость мяча
dt = 0.01  # Шаг времени
bounce = 0.9  # Коэффициент отскока (менее 1 для постепенного уменьшения высоты)

# Основной цикл анимации
while True:
    rate(100)  # Устанавливаем скорость анимации (100 кадров в секунду)

    # Обновляем скорость и позицию
    ball.velocity.y -= g * dt
    ball.pos += ball.velocity * dt

    # Проверяем, коснулся ли мяч платформы
    if ball.pos.y <= ball.radius and ball.velocity.y < 0:
        ball.velocity.y = -ball.velocity.y * bounce  # Меняем направление скорости с потерей энергии
