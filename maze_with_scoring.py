# Imports
import pygame
import intersects
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "HELL ON EARTH SIMULATOR"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Sounds
wah = pygame.mixer.Sound("waluigi.ogg")
pygame.mixer.music.load("asmr.ogg")

pygame.mixer.music.play(-1)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 25, 25)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (153, 51, 255)


# Make a player
player1 =  [0, 0, 25, 25]
player2 =  [WIDTH - 50, 0, 25, 25]
vel1 = [0, 0]
vel2 = [0, 0]
player1_speed = 8
player2_speed = 3
score1 = 0
score2 = 0

# Make walls
wall1 =  [25, 0, 25, HEIGHT - 25]
wall2 =  [75, 25, 25, HEIGHT - 25]
wall3 =  [125, 0, 25, HEIGHT - 25]
wall4 =  [175, 25, 25, HEIGHT - 25]
wall5 =  [225, 0, 25, HEIGHT - 25]
wall6 =  [275, 25, 25, HEIGHT - 25]
wall7 =  [325, 0, 25, HEIGHT - 25]
wall8 =  [375, 25, 25, HEIGHT - 25]
wall9 =  [425, 0, 25, HEIGHT - 25]
wall10 =  [475, 25, 25, HEIGHT - 25]
wall11 =  [525, 0, 25, HEIGHT - 25]
wall12 =  [575, 25, 25, HEIGHT - 25]
wall13 =  [625, 0, 25, HEIGHT - 25]
wall14 =  [675, 25, 25, HEIGHT - 25]
wall15 =  [725, 0, 25, HEIGHT - 25]
wall16 =  [775, 25, 25, HEIGHT - 25]
wall17 =  [825, 0, 25, HEIGHT - 25]
wall18 =  [875, 0, 25, HEIGHT - 25]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]
coin4 = [0, 300, 25, 25]
coin5 = [50, 300, 25, 25]
coin6 = [150, 200, 25, 25]
coin7 = [200, 500, 25, 25]
coin8 = [300, 200, 25, 25]
coin9 = [300, 400, 25, 25]
coin10 = [400, 400, 25, 25]
coin11 = [400, 500, 25, 25]
coin12 = [400, 100, 25, 25]
coin13 = [400, 300, 25, 25]
coin14 = [WIDTH - 50, 0, 25, 25]
coin15 = [WIDTH - 50, 50, 25, 25]
coin16 = [WIDTH - 50, 100, 25, 25]
coin17 = [WIDTH - 50, 150, 25, 25]
coin18 = [WIDTH - 50, 200, 25, 25]
coin19 = [WIDTH - 50, 250, 25, 25]
coin20 = [WIDTH - 50, 300, 25, 25]
coin21 = [WIDTH - 50, 350, 25, 25]
coin22 = [WIDTH - 50, 400, 25, 25]
coin23 = [WIDTH - 50, 450, 25, 25]
coin24 = [WIDTH - 50, 500, 25, 25]
coin25 = [WIDTH - 50, 550, 25, 25]
coin25 = [WIDTH - 150, 400, 25, 25]

coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20, coin21, coin22, coin23, coin24, coin25]


# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    up2 = pressed[pygame.K_w]
    down2 = pressed[pygame.K_s]
    left2 = pressed[pygame.K_a]
    right2 = pressed[pygame.K_d]


    if left:
        vel1[0] = -player1_speed
    elif right:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0

    if up:
        vel1[1] = -player1_speed
    elif down:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0

    if left2:
        vel2[0] = -player2_speed
    elif right2:
        vel2[0] = player2_speed
    else:
        vel2[0] = 0

    if up2:
        vel2[1] = -player2_speed
    elif down2:
        vel2[1] = player2_speed
    else:
        vel2[1] = 0
        
        
    # Game logic (Check for collisions, update points, etc.)

    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]
    player2[0] += vel2[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

        if intersects.rect_rect(player2, w):        
            if vel2[0] > 0:
                player2[0] = w[0] - player2[2]
            elif vel2[0] < 0:
                player2[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    player2[1] += vel2[1]
    
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]

        if intersects.rect_rect(player2, w):                    
            if vel2[1] > 0:
                player2[1] = w[1] - player2[3]
            if vel2[1]< 0:
                player2[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''
    if player1[0] < 0:
        player1[0] = 0
    elif player1[0] > WIDTH - player1[2]:
        player1[0] = WIDTH - player1[2]

    if player1[1] < 0:
        player1[1] = 0
    elif player1[1] > HEIGHT - player1[3]:
        player1[1] = HEIGHT - player1[3]

    if player2[0] < 0:
        player2[0] = 0
    elif player2[0] > WIDTH - player2[2]:
        player2[0] = WIDTH - player2[2]

    if player2[1] < 0:
        player2[1] = 0
    elif player2[1] > HEIGHT - player2[3]:
        player2[1] = HEIGHT - player2[3]



    ''' get the coins '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        wah.play()

    for c in coins:
        if intersects.rect_rect(player2, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player2, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score2 += 1
        wah.play()
        
    if len(coins) == 0:
        win = True
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(PURPLE)

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, YELLOW, player2)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, GREEN, c)
        
    if win:
        font = pygame.font.Font(None, 100)
        screen.fill(BLACK)
        if score1 > score2:
            text = font.render("Player 1 Wins!", 1, WHITE)
        elif score2 > score1:
            text = font.render("Player 2 Wins!", 1, WHITE)
        else:
            text = font.render("Tie?", 1, WHITE)

        screen.blit(text, [250, 250])

    font = pygame.font.Font(None, 48)
    text = font.render(str(score1), 1, BLACK)
    screen.blit(text, [0, 0])

    text = font.render(str(score2), 1, BLACK)
    screen.blit(text, [WIDTH - 50, 0])
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()

