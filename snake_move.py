import pygame
import time
import random

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.update()

open = True

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
x = random.randint(100, 500)
black = 0, 0, 0
y = random.randint(100, 500)
x_change = 0
y_change = 0

while open:
    x += x_change
    y += y_change
    display.fill(black)
    pygame.draw.circle(display, color, (x, y), 11, 0)
    time.sleep(0.1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change != -5:
                x_change = -5
                y_change = 0
            if event.key == pygame.K_LEFT and x_change == -5:
                print("left")
                x_change = -5
                y_change = 0
            if event.key == pygame.K_RIGHT and x_change != -5:
                x_change = 5
                y_change = 0    
            if event.key == pygame.K_RIGHT and x_change == -5:
                x_change = 5
                y_change = 0
            if event.key == pygame.K_UP and y_change != -5:
                x_change = 0
                y_change = -5
            if event.key == pygame.K_UP and y_change == -5:
                x_change = 0
                y_change = -5
            if event.key == pygame.K_DOWN and y_change != -5:
                x_change = 0
                y_change = 5
            if event.key == pygame.K_DOWN and y_change == -5:
                x_change = 0
                y_change = 5
        if event.type == pygame.QUIT:
            open = false
    pygame.display.update()


pygame.quit()
quit()