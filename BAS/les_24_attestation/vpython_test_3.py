from vpython import *

# Создаем окно с 3D-сценой и добавляем сферу
scene = canvas(title='Пример анимации с VPython', width=1920, height=1080)
sphere_obj = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.cyan)

# Устанавливаем скорость движения
velocity = vector(0.1, 0, 0)

# Бесконечный цикл для анимации движения
while True:
    rate(60)  # Устанавливаем частоту обновления 60 кадров в секунду
    sphere_obj.pos += velocity  # Обновляем положение сферы

    # Проверяем, чтобы сфера отскакивала от стен
    if abs(sphere_obj.pos.x) >= 5:
        velocity.x *= -1  # Меняем направление скорости
