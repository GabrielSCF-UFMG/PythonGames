import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (600, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Snake")

# Set the dimensions of the snake block
block_size = 20

# Set the font for displaying the score
font = pygame.font.Font(None, 30)

# Set the initial direction of the snake
direction = "right"

# Set the initial position of the snake
snake_position = [100, 100]

# Initialize the snake body
snake_body = [[100, 100], [80, 100], [60, 100]]

# Set the initial position of the food
food_position = [300, 300]
food_spawned = True

# Set the initial score to 0
score = 0

# Set the initial speed of the game
speed = 100

# Speed of the snake
speedSnake = 1

# Time countup limit to eat
count = 0

# Set the colors
red = pygame.Color(255, 0, 0)  # game over
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

# Set the game over flag to False
game_over = False

# Run the game loop
while not game_over:

    pygame.time.delay(speed)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
            if event.key == pygame.K_DOWN:
                direction = "down"
            if event.key == pygame.K_LEFT:
                direction = "left"
            if event.key == pygame.K_RIGHT:
                direction = "right"

    # Check if the snake has collided with the boundaries

    width_boundarie = (block_size * (int(score / 10)))

    if score <= 10:

        # Colliding the rigth boundarie
        if snake_position[0] > window_size[0] - block_size:
            snake_position[0] = 0

        #Colliding the lefth coundarie
        elif snake_position[0] < block_size:
            snake_position[0] = window_size[0]

        #Colliding the botton boundarie
        elif snake_position[1] > window_size[1] - block_size:
            snake_position[1] = 0 + block_size

        #Collidign the top boundarie
        elif snake_position[1] < 0:
            snake_position[1] = window_size[0]

    elif score > 10:

        if snake_position[0] > window_size[0] - block_size - width_boundarie or snake_position[0] < 0 + width_boundarie:
            game_over = True
        if snake_position[1] > window_size[1] - block_size - width_boundarie or snake_position[1] < 0 + width_boundarie:
            game_over = True

    # Check if the snake has collided with itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True

    # If the food has not been spawned, spawn it
    if not food_spawned:
        food_position = [random.randrange(1, (window_size[0] // block_size)) * block_size,
                         random.randrange(1, (window_size[1] // block_size)) * block_size]
        food_spawned = True

    count += 1

    if count >= 50*(1+int(score/10)):
        food_spawned = False
        count = 0

    # Move the snake
    if direction == "up":
        snake_position[1] -= block_size
    if direction == "down":
        snake_position[1] += block_size
    if direction == "left":
        snake_position[0] -= block_size
    if direction == "right":
        snake_position[0] += block_size

    # Insert the new snake position at the beginning of the snake_body list
    snake_body.insert(0, list(snake_position))

    # Check if the snake has eaten the food
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawned = False
        count = 0
    else:
        # Remove the last block of the snake
        snake_body.pop()

    # Changing the speed
    speed = int(100/(2**+int(score/10)))

    # Set the screen background
    screen.fill(white)

    # Draw the snake
    for position in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(position[0], position[1], block_size, block_size))

    # Draw the food
    pygame.draw.rect(screen, 'yellow', pygame.Rect(food_position[0], food_position[1], block_size, block_size))

    # Adding boundaries

    boundarie_rigth = pygame.draw.rect(screen, brown,(window_size[0] - width_boundarie, 0, width_boundarie, window_size[1]))
    boundarie_left = pygame.draw.rect(screen, brown, (0, 0, width_boundarie, window_size[1]))
    boundarie_top = pygame.draw.rect(screen, brown, (0, 0, window_size[0], width_boundarie))
    boundarie_bot = pygame.draw.rect(screen, brown, (0, window_size[0]-width_boundarie, window_size[0], width_boundarie))

    # Display the score
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, [0, 0])

    # Display the level
    score_text = font.render("Nivel "+str(int(score / 20)), True, black)
    screen.blit(score_text, [window_size[0]/2 - 50, 0])

    # Refresh the screen
    pygame.display.update()

    # Set the game speed
    pygame.time.delay(speed)

# Game Over message
game_over_text = font.render("Game Over!", True, red)
screen.blit(game_over_text, (250, 270))
pygame.display.update()
pygame.time.delay(3000)

# Quit the game
pygame.quit()
