# Example file showing a circle moving on screen
import pygame

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

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#A9A9A9")

    # Player 1 movement

    pygame.draw.circle(screen, "red", player1_pos, 40)

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

    pygame.draw.circle(screen, "blue", player2_pos, 40)

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
    
    pygame.draw.circle(screen, "yellow", player3_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_i]:
        player3_pos.y -= player3_speed * dt
    if keys[pygame.K_k]:
        player3_pos.y += player3_speed * dt
    if keys[pygame.K_j]:
        player3_pos.x -= player3_speed * dt
    if keys[pygame.K_l]:
        player3_pos.x += player3_speed * dt

    # keep player 3 circle within screen
    player3_pos.x = max(40, min(player3_pos.x, screen.get_width() - 40))
    player3_pos.y = max(40, min(player3_pos.y, screen.get_height() - 40))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000  

pygame.quit()
