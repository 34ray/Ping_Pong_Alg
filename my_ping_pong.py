from pygame import *
init()
from time import time as timer
import random

#класс - суперкласс для всех остальных
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_width, player_height):
        super().__init__()
        self.width = player_width
        self.height = player_height
        self.image = transform.scale(image.load(player_image), (self.width, self.height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
#класс игрока
class Player(GameSprite):
    def move_1(self):
        keys = key.get_pressed()
        # если нажата клавиша "стрелка вверх" и физическая модель не ушла за верхнюю границу игры
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        # если нажата клавиша "стрелка вниз" и физическая модель не ушла за нижнюю границу игры
        if keys[K_DOWN] and self.rect.y < height - 150:
            self.rect.y += self.speed
    # метод для управления игроком №1 (левая ракетка)
    def move_2(self):
        keys = key.get_pressed()
        # если нажата клавиша "W" и физическая модель не ушла за верхнюю границу игры
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        # если нажата клавиша "S" и физическая модель не ушла за нижнюю границу игры
        if keys[K_s] and self.rect.y < height - 150:
            self.rect.y += self.speed

# размеры окна
width = 600
height = 500

# создание окна
window = display.set_mode((width, height))
display.set_caption("Ping Pong")
back = (200, 0, 255) 
window.fill(back)  

clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont("Arial", 36)
lose1 = font1.render("Второй победил!", True, (180, 0, 0))
lose2 = font1.render("Первый победил!", True, (180, 0, 0))

rocket1 = Player("tabletenis.png", 4, 30, 200, 50, 150)
rocket2 = Player("tabletenis.png", 4, 520, 200, 50, 150)
ball = GameSprite("ball.png", 200, 200, 4, 50, 50)

# скорости мячика по вертикали и горизонтали
ball_x = 3
ball_y = 3

# переменная окончания игры
finish = False  
# переменная завершения программы
game = True  

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 

    if finish != True:
        window.fill(back)  
        rocket1.move_2()  
        rocket2.move_1()  

        # перемещение мячика
        ball.rect.x += ball_x
        ball.rect.y += ball_y

        if sprite.collide_rect(rocket1, ball):
            ball_x *= -1

        if sprite.collide_rect(rocket2, ball):
            ball_x *= -1

        if ball.rect.y < 0 or ball.rect.y > height - 50:
            ball_y *= -1

        if ball.rect.x < 0:
            finish = True  
            window.blit(lose1, (200, 200))  

        if ball.rect.x > width - 50:
            finish = True  
            window.blit(lose2, (200, 200))  

        rocket1.draw()  
        rocket2.draw()  
        ball.draw() 

    # обновляем все содержимое на экране
    display.update()
    clock.tick(FPS)