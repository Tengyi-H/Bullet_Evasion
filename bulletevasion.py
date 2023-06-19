import pygame
import random
import time

pygame.init()

def draw_text(text,font,color,surface,x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodge")



white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

font = pygame.font.SysFont(None, 50)

player_width = 50
player_height = 50
player_x = width / 2 - player_width / 2
player_y = height - player_height - 10
player_speed = 0.75

cake_width = 75
cake_height = 60
cake_x = random.randint(0, width - cake_width)
cake_y = 0
cake_speed = random.uniform(0.1,0.5)

candle_width = 25
candle_height = 50
candle_x = random.randint(0, width - candle_width)
candle_y = 0
candle_speed = random.uniform(0.5,1)

candle_width2 = 25
candle_height2 = 50
candle_x2 = random.randint(0, width - candle_width2)
candle_y2 = 0
candle_speed2 = random.uniform(0.5,1)

candle_width3 = 25
candle_height3 = 50
candle_x3 = random.randint(0, width - candle_width3)
candle_y3 = 0
candle_speed3 = random.uniform(0.5,1)

candle_width4 = 25
candle_height4 = 50
candle_x4 = random.randint(0, width - candle_width4)
candle_y4 = 0
candle_speed4 = random.uniform(0.5,1)

lives = 100000
score = 0

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    if lives == 0:
        time.sleep(1)
        pygame.quit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    cake_y += cake_speed
    candle_y += candle_speed
    candle_y2 += candle_speed2
    candle_y3 += candle_speed3
    candle_y4 += candle_speed4

    if player_x < cake_x + cake_width and player_x + player_width > cake_x and player_y < cake_y + cake_height and player_y + player_height > cake_y:
        score += 1
        cake_x = random.randint(0, width - cake_width)
        cake_y = 0
    elif player_y < cake_y:
        cake_x = random.randint(0, width - cake_width)
        cake_y = 0

    if player_x < candle_x + candle_width and player_x + player_width > candle_x and player_y < candle_y + candle_height and player_y + player_height > candle_y:
        lives -= 1
        candle_x = random.randint(0, width - candle_width)
    elif player_y < candle_y:
        candle_x = random.randint(0, width - candle_width2)
        candle_y = 0

    if player_x < candle_x2 + candle_width2 and player_x + player_width > candle_x2 and player_y < candle_y2 + candle_height2 and player_y + player_height > candle_y2:
        lives -= 1
        candle_x2 = random.randint(0, width - candle_width2)
    elif player_y < candle_y2:
        candle_x2 = random.randint(0, width - candle_width3)
        candle_y2 = 0

    if player_x < candle_x3 + candle_width3 and player_x + player_width > candle_x3 and player_y < candle_y3 + candle_height3 and player_y + player_height > candle_y3:
        lives -= 1
        candle_x3 = random.randint(0, width - candle_width3)
    elif player_y < candle_y3:
        candle_x3 = random.randint(0, width - candle_width3)
        candle_y3 = 0

    if player_x < candle_x4 + candle_width4 and player_x + player_width > candle_x4 and player_y < candle_y4 + candle_height4 and player_y + player_height > candle_y4:
        lives -= 1
        candle_x4 = random.randint(0, width - candle_width4)
    elif player_y < candle_y4:
        candle_x4 = random.randint(0, width - candle_width4)
        candle_y4 = 0

    window.fill(white)
    pygame.draw.rect(window, black, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(window, green, (cake_x, cake_y, cake_width, cake_height))
    pygame.draw.rect(window, red, (candle_x, candle_y, candle_width, candle_height))
    pygame.draw.rect(window, red, (candle_x2, candle_y2, candle_width2, candle_height2))
    pygame.draw.rect(window, red, (candle_x3, candle_y3, candle_width3, candle_height3))
    pygame.draw.rect(window, red, (candle_x4, candle_y4, candle_width4, candle_height4))

    score_text = font.render("Score: " + str(score), True, black)
    window.blit(score_text, (10, 10))

    lives_text = font.render("Lives Left: " + str(lives), True, black)
    window.blit(lives_text, (550, 10))

    pygame.display.update()

pygame.quit()
