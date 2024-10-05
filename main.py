import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))



pygame.display.set_caption("Game Tir")
icon = pygame.image.load("boez.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/klipartz.com (3).png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0,SCREEN_HEIGHT-target_height)

color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))


score = 0
font = pygame.font.Font(None, 36)




running = True
while running:
    screen.fill(color)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <mouse_x< target_x + target_width and target_y <mouse_y <target_y+target_height:
                target_x = random.randint(0,SCREEN_WIDTH+target_width)
                target_y = random.randint(0, SCREEN_HEIGHT+target_height)
                score +=1
    screen.blit(target_img, (target_x, target_y))



    pygame.display.update()


pygame.quit()