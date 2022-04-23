import pygame
import time
import random
from pygame.locals import * 


pygame.init()

score = 0

# Setting dimensions
d_width = 500
d_height = 500
s_length = 30
display = pygame.display.set_mode((d_width, d_height))
pygame.display.update()

win = pygame.display.set_mode((d_width, d_height))
largeFont = pygame.font.SysFont('comicsans', 20) # creates a font object


end_of_game = False

#Snake Functions
color = (65, 204, 20)

#Snake x and y starting coordinates
x = random.randint(100, 400)
black = 0, 0, 0
y = random.randint(100, 400)
snake_body= [(x,y)]
x_change = 0
y_change = 0

#The food is a rectangle. Rectangle Code:
food_color = (211, 36, 36)
foodx = (random.randint(100, 400))
foody = (random.randint(100, 400))
def drawfood(foodx, foody):
    food1 = Rect(foodx, foody, 10, 10)
    food = pygame.draw.rect(display, food_color, food1, 5)
snake_length = 20
snake_width =  20

#snake= Rect (x, y, snake_length, snake_length)
eat_food = False
first = True

# Snake can move with arrow keys
while not end_of_game:
    x += x_change
    y += y_change
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 5
                y_change = 0    
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -5
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 5
            first = False 
        if event.type == pygame.QUIT:
            print ("Quit Event")
            end_of_game = True    
    if not first and (x+x_change, y+y_change) in snake_body:
        pygame.quit()
        break 
    if x >= d_width or x < 0 or y >= d_height or y < 0:
        end_of_game = True
    display.fill(black)
    drawfood(foodx, foody)
    snake_body.append((x + x_change, y + y_change))

    # Keeping track of score
    if not eat_food:
        snake_body.pop(0)
    if eat_food:
        eat_food = False 
        score += 1
    text = largeFont.render('Score: ' + str(score), 1, (100,100,100))
    display.blit(text, [0, 0])


    #snake= pygame.draw.rect(display, color, newsnake) 
    for pos in snake_body:
        newsnake= Rect (pos[0], pos[1], 10, 10)
        pygame.draw.rect (display, color, newsnake)
    time.sleep(0.1)
    pygame.display.update() 
    if (abs(x - foodx) <=10)  and (abs(y - foody) <=10):
        foodx = (random.randint(100, 400))
        foody = (random.randint(100, 400))
        drawfood(foodx, foody)
        eat_food = True
pygame.quit()
quit()