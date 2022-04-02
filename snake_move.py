import pygame
import time
import random
from pygame.locals import * 



pygame.init()

d_width = 900
d_height = 700
s_length = 30
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

foodx = (random.randint(100, 500))
foody = (random.randint(100, 500))

food = Rect(foodx, foody, 10, 10)

snake_length = 20
snake_width =  20

snake= Rect (x, y, snake_length, snake_length)

while not end_of_game:
    x += x_change
    y += y_change
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change != -5:
                x_change = -5
                y_change = 0
            elif event.key == pygame.K_LEFT and x_change == -5:
                print("left")
                x_change = -5
                y_change = 0
            elif event.key == pygame.K_RIGHT and x_change != -5:
                print("right")
                x_change = 5
                y_change = 0    
            elif event.key == pygame.K_RIGHT and x_change == -5:
                x_change = 5
                y_change = 0
            elif event.key == pygame.K_UP and y_change != -5:
                print("up")
                x_change = 0
                y_change = -5
            elif event.key == pygame.K_UP and y_change == -5:
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
            print ("Quit Event")
            end_of_game = True
        
    if x >= d_width or x < 0 or y >= d_height or y < 0:
        end_of_game = True
        

    display.fill(black)

    food = pygame.draw.rect(display, food_color, food, 1)
    
    newsnake= Rect (x + x_change, y + y_change, snake_length, snake_width)

    snake= pygame.draw.rect(display, color, newsnake) 


#if pygame.Rect.collidedict(snake, food) == True:
    #print ("Found Food!") 



    time.sleep(0.1)
    pygame.display.update() 


    print ("X is ", x)
    print ("Y is ", y) 

    print ("Foodx is ", foodx)
    print ("Foody is ", foody)

    if (abs(x - foodx) <=10)  and (abs(y - foody) <=10):
       print ("Found Food!") 
       snake_length = snake_length + 1

pygame.quit()
quit()
