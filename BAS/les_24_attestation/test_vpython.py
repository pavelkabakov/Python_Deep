from vpython import *

# Создаем окно для отображения 3D-сцены
scene = canvas(title='Простая анимация сферы')

# Создаем сферу (мяч) и пол
ball = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.red)
floor = box(pos=vector(0, -0.5, 0), size=vector(12, 0.1, 4), color=color.green)

# Устанавливаем начальную скорость
ball.velocity = vector(1, 0, 0)

# Основной цикл анимации
dt = 0.01
while True:
    rate(100)  # Задает скорость анимации (100 кадров в секунду)
    # Обновляем позицию мяча
    ball.pos += ball.velocity * dt

    # Если мяч достигает края платформы, меняем направление
    if abs(ball.pos.x) > 5.5:
        ball.velocity.x = -ball.velocity.x
