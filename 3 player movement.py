# Example file showing a circle moving on screen
import pygame
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#set player starting positions by spawning them at half of the creens height and width
player1_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player3_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#set player speeds
player1_speed = 300
player2_speed = 300
player3_speed = 1200

#set player colours
player1_col = "#FF0000FF"
player2_col = "#0800FFFF"
player3_col = "#F6FF00FF"

# set tag variables   
players = ["player1", "player2","player3"]
it = random.choice(players)

def check_collisions(player):
    if pygame.rect.collide

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#FFFFFF")

    # Player 1 movement

    pygame.draw.circle(screen, player1_col, player1_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_pos.y -= player1_speed * dt
    if keys[pygame.K_s]:
        player1_pos.y += player1_speed * dt
    if keys[pygame.K_a]:
        player1_pos.x -= player1_speed * dt
    if keys[pygame.K_d]:
        player1_pos.x += player1_speed * dt

    # keep player 1 circle within screen

    player1_pos.x = max(40, min(player1_pos.x, screen.get_width() - 40))
    player1_pos.y = max(40, min(player1_pos.y, screen.get_height() - 40))

    # Player 2 movement

    pygame.draw.circle(screen, player2_col, player2_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2_pos.y -= player2_speed * dt
    if keys[pygame.K_DOWN]:
        player2_pos.y += player2_speed * dt
    if keys[pygame.K_LEFT]:
        player2_pos.x -= player2_speed * dt
    if keys[pygame.K_RIGHT]:
        player2_pos.x += player2_speed * dt

    # keep player 2 circle within screen

    player2_pos.x = max(40, min(player2_pos.x, screen.get_width() - 40))
    player2_pos.y = max(40, min(player2_pos.y, screen.get_height() - 40))

    # Player 3 movement
    
    pygame.draw.circle(screen, player3_col, player3_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_i]:
        player3_pos.y -= player3_speed * dt
    if keys[pygame.K_k]:
        player3_pos.y += player3_speed * dt
    if keys[pygame.K_j]:
        player3_pos.x -= player3_speed * dt
    if keys[pygame.K_l]:
        player3_pos.x += player3_speed * dt

    #keep player 3 circle within screen
    player3_pos.x = max(40, min(player3_pos.x, screen.get_width() - 40))
    player3_pos.y = max(40, min(player3_pos.y, screen.get_height() - 40))
    
    #check player collisions


    #run tag game

    if it == "player1":

        set('it' "player1")
        for i in range (1):
            print(f'{it} is it')

    elif it == "player2":

        set('it' "player2")
        for i in range (1):
            print(f'{it} is it')

    elif it == "player3":

        set('it' "player3")
        for i in range (1):
            print(f'{it} is it')  

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000  

pygame.quit()
