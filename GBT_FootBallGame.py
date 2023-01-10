import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Football')

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Set up the field dimensions
field_width = 800
field_height = 600

# Set up the goal dimensions
goal_width = 200
goal_height = 50

# Set up the player dimensions
player_width = 50
player_height = 50

# Set up the ball dimensions
ball_size = 20

# Set up the initial positions of the players and ball
player1_x = 20
player1_y = field_height / 2 - player_height / 2
player2_x = field_width - player_width - 20
player2_y = field_height / 2 - player_height / 2
ball_x = field_width / 2 - ball_size / 2
ball_y = field_height / 2 - ball_size / 2

# Set up the initial possession of the ball
possession = 1

# Set up the initial scores
score1 = 0
score2 = 0

# Run the game loop
running = True
while running:
    # Fill the screen with green
    screen.fill(green)

    # Draw the goals
    pygame.draw.rect(screen, white, (0, field_height / 2 - goal_height / 2, goal_width, goal_height))
    pygame.draw.rect(screen, white, (field_width - goal_width, field_height / 2 - goal_height / 2, goal_width, goal_height))

    # Draw the players
    pygame.draw.rect(screen, white, (player1_x, player1_y, player_width, player_height))
    pygame.draw.rect(screen, white, (player2_x, player2_y, player_width, player_height))

    # Draw the ball
    pygame.draw.circle(screen, white, (int(ball_x), int(ball_y)), ball_size)

    # Update the display
    pygame.display.flip()

    speed = 20
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Player 1 moves with the arrow keys
            if event.key == pygame.K_UP:
                player1_y = max(0, player1_y - speed)
            if event.key == pygame.K_DOWN:
                player1_y = max(0, player1_y + speed)
            if event.key == pygame.K_RIGHT:
                player1_x = max(0, player1_x + speed )
            if event.key == pygame.K_LEFT:
                player1_x = max(0, player1_x - speed)

            # Player 2 moves with the arrow keys
            if event.key == pygame.K_w:
                player2_y = max(0, player2_y - speed)
            if event.key == pygame.K_s:
                player2_y = max(0, player2_y + speed)
            if event.key == pygame.K_d:
                player2_x = max(0, player2_x + speed)
            if event.key == pygame.K_a:
                player2_x = max(0, player2_x - speed)
