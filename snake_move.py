import pygame
import time
import random
from pygame.locals import * 



pygame.init()

d_width = 900
d_height = 700
display = pygame.display.set_mode((d_width, d_height))
pygame.display.update()

end_of_game = False

#Snake Functions
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#Snake x and y starting coordinates
x = random.randint(100, 500)
black = 0, 0, 0
y = random.randint(100, 500)

x_change = 0
y_change = 0

#The food is a rectangle. Rectangle Code:

food_color = (28, 127, 151)

rectx = (random.randint(500, 500))
recty = (random.randint(500, 500))

rect0 = Rect(rectx, recty, 10, 10)

while not end_of_game:
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
                print("right")
                x_change = 5
                y_change = 0    
            if event.key == pygame.K_RIGHT and x_change == -5:
                x_change = 5
                y_change = 0
            if event.key == pygame.K_UP and y_change != -5:
                print("up")
                x_change = 0
                y_change = -5
            if event.key == pygame.K_UP and y_change == -5:
                x_change = 0
                y_change = -5
            if event.key == pygame.K_DOWN and y_change != -5:
                print("down")
                x_change = 0
                y_change = 5
            if event.key == pygame.K_DOWN and y_change == -5:
                x_change = 0
                y_change = 5
        
        if event.type == pygame.QUIT:
            end_of_game = False
        
    if x >= d_width or x < 0 or y >= d_height or y < 0:
        end_of_game = True
        
    pygame.draw.rect(display, food_color, rect0, 1)
    pygame.display.update()

    pygame.display.update()




pygame.quit()
quit()
