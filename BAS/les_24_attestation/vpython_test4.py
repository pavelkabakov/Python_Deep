
from vpython import sphere, vector, rate

# Создаем шарик
ball = sphere(pos=vector(0, 10, 0), radius=1, color=vector(1, 0, 0))

# Начальные условия
velocity = vector(0, -1, 0) # начальная скорость
g = vector(0, -9.8, 0) # ускорение свободного падения
dt = 0.01 # шаг времени

while True:
    rate(100) # управление скоростью анимации

    # Обновляем позицию шарика
    ball.pos = ball.pos + velocity * dt

    # Обновляем скорость шарика
    velocity = velocity + g * dt

    # Проверяем столкновение с землей
    if ball.pos.y < ball.radius:
        velocity.y = -velocity.y # меняем направление скорости на противоположное
