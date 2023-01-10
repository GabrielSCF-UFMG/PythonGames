import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (1000, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Obstacle Game")

# Set the background color
bg_color = pygame.Color("gray")

# Create a player image
player_image = pygame.image.load("guerreiro.png")

# Set the initial position of the player
player_x = 100
player_y = 150

# Set the speed of the player
player_speed = 50

# Set the size of the obstacles
obstacle_size = (20, 20)

# Create a list to store the obstacles
obstacles = []

# Max obstacles
maxObstacles = 10

# Set the initial positions of the obstacles
for i in range(maxObstacles):
    x = 400 + i * 50
    y = random.randint(0, 300 - obstacle_size[1])
    obstacles.append((x, y))

# Set the speed of the obstacles
obstacle_speed = player_speed/2

# Set the font for the game over text
font = pygame.font.Font(None, 36)

# Set the game over flag to False
game_over = False

# Run the game loop
while not game_over:

    pygame.time.delay(100)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y -= player_speed
            elif event.key == pygame.K_DOWN:
                player_y += player_speed
            elif event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed

    # Update the obstacle positions
    for i, obstacle in enumerate(obstacles):
        x, y = obstacle
        x -= obstacle_speed
        obstacles[i] = (x, y)

    # Remove the obstacles that have moved off the screen
    obstacles = [obstacle for obstacle in obstacles if obstacle[0] > 0]

    # Add a new obstacle
    if len(obstacles) <= maxObstacles/2 or obstacles[-1][0] < 300:
        x = window_size[0]
        y = random.randint(0, 300 - obstacle_size[1])
        obstacles.append((x, y))

    # Check for collision with an obstacle
    for obstacle in obstacles:
        if player_x + player_image.get_width() > obstacle[0] and player_x < obstacle[0] + obstacle_size[0]:
            if player_y + player_image.get_height() > obstacle[1] and player_y < obstacle[1] + obstacle_size[1]:
                game_over = True

    # Draw the background
    screen.fill(bg_color)

    # Draw the player
    screen.blit(player_image, (player_x, player_y))

    # Draw the obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, pygame.Color("red"), (obstacle[0],obstacle[1], obstacle_size[0], obstacle_size[1]))#obstacle[0], obstacle[1], obstacle_size[0], obstacle_size[1]))

    # Update the display
    pygame.display.update()

# Display the game over screen
game_over_text = font.render("Game Over", True, pygame.Color("black"))
text_rect = game_over_text.get_rect()
text_rect.center = (200, 150)
screen.blit(game_over_text, text_rect)
pygame.display.update()

# Wait for the player to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
    if game_over:
        break

# Quit Pygame
pygame.quit()
