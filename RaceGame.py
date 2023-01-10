import random

import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (1000, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Race Game")

# Set the background color
bg_color = pygame.Color("gray")

# Create a car image
car_image = pygame.image.load("carro.png")

# Set the initial position of the car
car_x = 0
car_y = 100

# Set the speed of the car
car_speed = 50

# Set the size of the obstacles
obstacle_size = (20, 20)

# Create a list to store the obstacles
obstacles = []

# Timer
timer = 0


# Set the initial positions of the obstacles
for i in range(10):
    x = window_size[0] + i * 50#400 + i * 50
    y = random.randint(0,window_size[1])
    obstacles.append((x, y))

# Set the speed of the obstacles
obstacle_speed = car_speed/2

# Set the font for the game over text
font = pygame.font.Font(None, 36)

# Set the game over flag to False
game_over = False

# Run the game loop

def gameLoop():

    global car_x, car_y, timer, game_over, obstacles,event

    while not game_over:

        pygame.time.delay(100)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    car_y -= car_speed
                if event.key == pygame.K_DOWN:
                    car_y += car_speed
                if event.key == pygame.K_RIGHT:
                    car_x += car_speed
                if event.key == pygame.K_LEFT:
                    car_x -= car_speed

        # Update the car position
        #car_x += car_speed

        # Update time
        timer += 1

        # Update the obstacle positions
        for i, obstacle in enumerate(obstacles):
            x, y = obstacle
            x -= obstacle_speed
            obstacles[i] = (x, y)

        # Remove the obstacles that have moved off the screen
        obstacles = [obstacle for obstacle in obstacles if obstacle[0] > 0]

        # Add a new obstacle
        if len(obstacles) <= 8 or obstacles[-1][0] < 300:
            x = window_size[0]
            y = random.randint(0,window_size[1])
            obstacles.append((x, y))

        # Check for collision with an obstacle
        for obstacle in obstacles:
            if car_x + car_image.get_width() > obstacle[0] and car_x < obstacle[0] + obstacle_size[0]:
                if car_y + car_image.get_height() > obstacle[1] and car_y < obstacle[1] + obstacle_size[1]:
                    game_over = True

        # Draw the background
        screen.fill(bg_color)

        # Draw the car
        screen.blit(car_image, (car_x, car_y))

        # Draw the obstacles
        tipo_roda = 0
        for obstacle in obstacles:
            tipo_roda += 1
            #pygame.draw.circle(screen, pygame.Color("black"), (obstacle[0] + obstacle_size[0]/2, obstacle[1] + obstacle_size[0]/2), obstacle_size[0]/2)
            if tipo_roda % 2 == 0:
                roda_image = pygame.image.load("roda1.png")
                screen.blit(roda_image, (obstacle[0], obstacle[1]))
            elif tipo_roda % 3 == 0:
                roda_image = pygame.image.load("roda2.png")
                screen.blit(roda_image, (obstacle[0], obstacle[1]))
            else:
                roda_image = pygame.image.load("roda3.png")
                screen.blit(roda_image, (obstacle[0], obstacle[1]))
            #pygame.draw.rect(screen, pygame.Color("red"), (obstacle[0], obstacle[1], obstacle_size[0], obstacle_size[1]))



        # Check if the player has reached the finish line
        if car_x > window_size[0] and timer > 500:
            game_over = True

        # Update the display
        pygame.display.update()
        verificaGameOver()

def verificaGameOver():

    global game_over

    # Display the game over screen
    if game_over == True:
        screen.fill("white")
        game_over_text = font.render("Game Over", True, pygame.Color("black"))
        text_rect = game_over_text.get_rect()
        text_rect.center = (window_size[0]/2, window_size[1]/2)
        screen.blit(game_over_text, text_rect)
        print(game_over)

    else:
        game_timer_text = font.render("Points: "+str(timer),True,pygame.Color("black"))
        text_rect = game_timer_text.get_rect()
        text_rect.center = (100, window_size[1]-50)
        screen.blit(game_timer_text, text_rect)

    pygame.display.update()

# Wait for the player to close the window

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #game_over = True
            break
        elif game_over == False or (game_over == True and event.type == pygame.K_CAPSLOCK):
            print(game_over)
            gameLoop()


    #if game_over:
    #    break



# Quit Pygame
pygame.quit()
