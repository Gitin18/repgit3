import pygame
import random
import os
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("game tir")

icon = pygame.image.load("image/boez2.jpg")

pygame.display.set_icon(icon)

screen.blit(icon, (400,300))  # Отображает изображение на экране в позиции (0, 0)
pygame.display.update()    # Обновляет экран


target_img = pygame.image.load("image/terget.png.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)

color = (random.randint(0,225), random.randint(0,225),random.randint(0,225))

running = True
while running:
    pass

pygame.quit()