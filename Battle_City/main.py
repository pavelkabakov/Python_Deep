import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle City")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Частота обновления экрана
clock = pygame.time.Clock()
FPS = 60

# Класс для танка
class Tank:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.color = color
        self.speed = 4
        self.direction = "UP"
        self.bullets = []

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = "UP"
        if keys[pygame.K_s]:
            self.y += self.speed
            self.direction = "DOWN"
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = "LEFT"
        if keys[pygame.K_d]:
            self.x += self.speed
            self.direction = "RIGHT"

    def shoot(self):
        # Добавляем пулю
        bullet = Bullet(self.x + self.width // 2, self.y + self.height // 2, self.direction)
        self.bullets.append(bullet)

# Класс для пули
class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 5
        self.speed = 8
        self.color = RED
        self.direction = direction

    def move(self):
        if self.direction == "UP":
            self.y -= self.speed
        elif self.direction == "DOWN":
            self.y += self.speed
        elif self.direction == "LEFT":
            self.x -= self.speed
        elif self.direction == "RIGHT":
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Основной игровой цикл
def main():
    run = True
    player = Tank(WIDTH // 2, HEIGHT // 2, GREEN)
    enemy = Tank(100, 100, BLUE)

    while run:
        clock.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Движение игрока
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Обновление пуль
        for bullet in player.bullets[:]:
            bullet.move()
            if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
                player.bullets.remove(bullet)

        # Отрисовка
        player.draw(screen)
        enemy.draw(screen)
        for bullet in player.bullets:
            bullet.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
