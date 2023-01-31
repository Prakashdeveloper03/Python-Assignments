import pygame

# Initialize pygame
pygame.init()

# Set window size
width, height = 640, 480

# Create window
screen = pygame.display.set_mode((width, height))

# Set background color to white
screen.fill((255, 255, 255))

# Define center, radius and speed of the ball
center = [width // 2, height // 2]
radius = 24
speed = [1, 1]

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update center based on speed
    center[0] += speed[0]
    center[1] += speed[1]

    # Reverse speed if ball hits a wall
    if center[0] + radius >= width or center[0] - radius <= 0:
        speed[0] = -speed[0]
    if center[1] + radius >= height or center[1] - radius <= 0:
        speed[1] = -speed[1]

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw ball
    pygame.draw.circle(screen, (255, 0, 0), center, radius)

    # Update screen
    pygame.display.update()

# Quit pygame
pygame.quit()
