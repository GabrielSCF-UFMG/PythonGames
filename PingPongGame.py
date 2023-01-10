import random
import pygame
import math

# Initialize pygame
pygame.init()

# Set the window size
screen_width = 1000
screen_height = 500

# Create the window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Ping Pong')

# Set up the game's colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the paddles
pad_width = 15
pad_height = 100

# Set the horizontal position of the paddles
pad_left_x = 20
pad_right_x = screen_width - pad_width - 20

# Set the vertical position of the paddles
pad_left_y = (screen_height / 2) - (pad_height / 2)
pad_right_y = (screen_height / 2) - (pad_height / 2)

# Set the paddle speeds
pad_speed = 5

# Set up the ball
ball_width = 20

# Set the initial position of the ball
ball_x = (screen_width / 2) - (ball_width / 2)
ball_y = (screen_height / 2) - (ball_width / 2)

# Set the ball's speed and direction
ball_speed_x = 5
ball_speed_y = 5

# Set the score
left_score = 0
right_score = 0

# Set the font
font = pygame.font.Font(None, 74)

# Set the game's clock
clock = pygame.time.Clock()

# Set up the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle keyboard input
    keys = pygame.key.get_pressed()

    # Move the left paddle
    commandRandom = random.randint(0,1)
    if commandRandom == 0:#keys[pygame.K_w]:
        pad_left_y -= pad_speed*2*right_score/10
    elif commandRandom == 1:#keys[pygame.K_s]:
        pad_left_y += pad_speed*2*right_score/10

    commandRandom2 = random.randint(0, 1)

    # Move the right paddle
    if keys[pygame.K_UP]:
        pad_right_y -= pad_speed
    elif keys[pygame.K_DOWN]:
        pad_right_y += pad_speed
    #if commandRandom == 0:#keys[pygame.K_w]:
    #    pad_right_y -= pad_speed*2*left_score
    #elif commandRandom == 1:#keys[pygame.K_s]:
    #    pad_right_y += pad_speed*2*left_score

    # Keep the paddles on the screen
    if pad_left_y < 0:
        pad_left_y = 0
    elif pad_left_y > screen_height - pad_height:
        pad_left_y = screen_height - pad_height

    if pad_right_y < 0:
        pad_right_y = 0
    elif pad_right_y > screen_height - pad_height:
        pad_right_y = screen_height - pad_height

    # Update the ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for ball collision with paddles
    if ball_x < pad_left_x + pad_width and ball_y > pad_left_y and ball_y < pad_left_y + pad_height:
        ball_speed_x = -ball_speed_x

    if ball_x > pad_right_x-pad_width and ball_y > pad_right_y and ball_y < pad_right_y + pad_height:
        ball_speed_x = -ball_speed_x

    # Check for ball collision with top and bottom of screen
    if ball_y < 0:
        ball_speed_y = -ball_speed_y
    elif ball_y > screen_height - ball_width:
        ball_speed_y = -ball_speed_y

    # Check for ball going off the left and right sides of the screen
    if ball_x < 0:
        right_score += 1
        ball_x = (screen_width / 2) - (ball_width / 2)
        ball_y = (screen_height / 2) - (ball_width / 2)
        ball_speed_x = 5 * (1 + abs(right_score-left_score)/25)
        ball_speed_y = 5 * (1 + abs(right_score-left_score)/25)

    elif ball_x > screen_width - ball_width:
        left_score += 1
        ball_x = (screen_width / 2) - (ball_width / 2)
        ball_y = (screen_height / 2) - (ball_width / 2)
        #ball_speed_x = -5
        #ball_speed_y = 5
        ball_speed_x = -(5 * (1 + abs(right_score - left_score) / 10))
        ball_speed_y = -(5 * (1 + abs(right_score - left_score) / 10))

    # Draw the screen
    screen.fill(color=(0,128,128))
    pygame.draw.rect(screen, "grey", (screen_width/2,0, 10,screen_height))
    pygame.draw.rect(screen, WHITE, (pad_left_x, pad_left_y, pad_width, pad_height))
    pygame.draw.rect(screen, WHITE, (pad_right_x, pad_right_y, pad_width, pad_height))
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, ball_width, ball_width))

    # Draw the scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (screen_width / 4, 0))
    screen.blit(right_text, (screen_width * 3 / 4, 0))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)
