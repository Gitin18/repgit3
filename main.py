import pygame
import random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("game tir")
icon = pygame.image.load("https://www.google.com/interests/saved/list/snjwRX5rmtW2xDfqsaqtSyJAYB-gqQ?hl=ru&q=%D0%98%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5+%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F&sa=X&ved=2ahUKEwjZifOt7PKIAxUt5r4IHbIBD68Q5oAKegQIARAf")
pygame.display.set_icon(icon)

##target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)

color = (random.randint(0,225), random.randint(0,225),random.randint(0,225))

running = True
while running:
    pass

pygame.quit()