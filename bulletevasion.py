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

treasure_width = 75
treasure_height = 60
treasure_x = random.randint(0, width - treasure_width)
treasure_y = 0
treasure_speed = random.uniform(0.1,0.5)

bullet_width = 25
bullet_height = 50
bullet_x = random.randint(0, width - bullet_width)
bullet_y = 0
bullet_speed = random.uniform(0.5,1)

bullet_width2 = 25
bullet_height2 = 50
bullet_x2 = random.randint(0, width - bullet_width2)
bullet_y2 = 0
bullet_speed2 = random.uniform(0.5,1)

bullet_width3 = 25
bullet_height3 = 50
bullet_x3 = random.randint(0, width - bullet_width3)
bullet_y3 = 0
bullet_speed3 = random.uniform(0.5,1)

bullet_width4 = 25
bullet_height4 = 50
bullet_x4 = random.randint(0, width - bullet_width4)
bullet_y4 = 0
bullet_speed4 = random.uniform(0.5,1)

lives = 3
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

    treasure_y += treasure_speed
    bullet_y += bullet_speed
    bullet_y2 += bullet_speed2
    bullet_y3 += bullet_speed3
    bullet_y4 += bullet_speed4

    if player_x < treasure_x + treasure_width and player_x + player_width > treasure_x and player_y < treasure_y + treasure_height and player_y + player_height > treasure_y:
        score += 1
        treasure_x = random.randint(0, width - treasure_width)
        treasure_y = 0
    elif player_y < treasure_y:
        treasure_x = random.randint(0, width - treasure_width)
        treasure_y = 0

    if player_x < bullet_x + bullet_width and player_x + player_width > bullet_x and player_y < bullet_y + bullet_height and player_y + player_height > bullet_y:
        lives -= 1
        bullet_x = random.randint(0, width - bullet_width)
    elif player_y < bullet_y:
        bullet_x = random.randint(0, width - bullet_width)
        bullet_y = 0

    if player_x < bullet_x2 + bullet_width2 and player_x + player_width > bullet_x2 and player_y < bullet_y2 + bullet_height2 and player_y + player_height > bullet_y2:
        lives -= 1
        bullet_x2 = random.randint(0, width - bullet_width2)
    elif player_y < bullet_y2:
        bullet_x2 = random.randint(0, width - bullet_width3)
        bullet_y2 = 0

    if player_x < bullet_x3 + bullet_width3 and player_x + player_width > bullet_x3 and player_y < bullet_y3 + bullet_height3 and player_y + player_height > bullet_y3:
        lives -= 1
        bullet_x3 = random.randint(0, width - bullet_width3)
    elif player_y < bullet_y3:
        bullet_x3 = random.randint(0, width - bullet_width3)
        bullet_y3 = 0

    if player_x < bullet_x4 + bullet_width4 and player_x + player_width > bullet_x4 and player_y < bullet_y4 + bullet_height4 and player_y + player_height > bullet_y4:
        lives -= 1
        bullet_x4 = random.randint(0, width - bullet_width4)
    elif player_y < bullet_y4:
        bullet_x4 = random.randint(0, width - bullet_width4)
        bullet_y4 = 0

    window.fill(white)
    pygame.draw.rect(window, black, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(window, green, (treasure_x, treasure_y, treasure_width, treasure_height))
    pygame.draw.rect(window, red, (bullet_x, bullet_y, bullet_width, bullet_height))
    pygame.draw.rect(window, red, (bullet_x2, bullet_y2, bullet_width2, bullet_height2))
    pygame.draw.rect(window, red, (bullet_x3, bullet_y3, bullet_width3, bullet_height3))
    pygame.draw.rect(window, red, (bullet_x4, bullet_y4, bullet_width4, bullet_height4))

    score_text = font.render("Score: " + str(score), True, black)
    window.blit(score_text, (10, 10))

    lives_text = font.render("Lives Left: " + str(lives), True, black)
    window.blit(lives_text, (550, 10))

    pygame.display.update()

pygame.quit()
