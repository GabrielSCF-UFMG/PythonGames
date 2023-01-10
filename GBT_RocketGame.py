import pygame
import math

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (1000, 500)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Rocket Game")

# Set the background color
bg_color = pygame.Color("black")

# Create a rocket image
rocket_image = pygame.image.load("rocket.png")

# Set the initial position of the rocket
rocket_x = 200
rocket_y = 150

# Set the speed of the rocket
rocket_speed = 3

# Set the initial angle of the rocket
rocket_angle = 0

# Set the rotation speed of the rocket
rocket_rotation_speed = 5

# Set the thrust flag to False
thrust = False

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
            if event.key == pygame.K_LEFT:
                rocket_angle -= rocket_rotation_speed
            elif event.key == pygame.K_RIGHT:
                rocket_angle += rocket_rotation_speed
            elif event.key == pygame.K_UP:
                thrust = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                thrust = False

    # Update the rocket position
    if thrust:
        rocket_x += math.cos(math.radians(rocket_angle)) * rocket_speed
        rocket_y -= math.sin(math.radians(rocket_angle)) * rocket_speed

    # Check if the rocket has left the screen
    if rocket_x < 0 or rocket_x > 400 or rocket_y < 0 or rocket_y > 300:
        game_over = True

    # Draw the background
    screen.fill(bg_color)

    # Draw the rocket
    rotated_rocket = pygame.transform.rotate(rocket_image, rocket_angle)
    rect = rotated_rocket.get_rect()
    rect.center = (rocket_x, rocket_y)
    screen.blit(rotated_rocket, rect)

    # Update the display
    pygame.display.update()

# Display the game over screen
game_over_text = font.render("Game Over", True, pygame.Color("white"))
text_rect = game_over_text.get_rect()
text_rect.center = (200, 150)
screen.blit(game_over_text, text_rect)
pygame.display.update()

# Wait for the player to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
