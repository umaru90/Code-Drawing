import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Balloons")

# Set up the balloon properties
balloon_radius = 30
balloon_color = (255, 0, 0)  # Red color
balloon_speed = 1  # Speed of the balloons

# Create a list to store balloon objects
balloons = []

class Balloon:
    def __init__(self):
        self.radius = balloon_radius
        self.color = balloon_color
        self.x = random.randint(self.radius, width - self.radius)
        self.y = height
        self.speed = random.randint(1, 3)
    
    def update(self):
        self.y -= self.speed
        if self.y < -self.radius:
            self.y = height
            self.x = random.randint(self.radius, width - self.radius)
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


# Create multiple balloon objects
num_balloons = 10
for _ in range(num_balloons):
    balloon = Balloon()
    balloons.append(balloon)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((255, 255, 255))  # White background
    
    # Update and draw balloons
    for balloon in balloons:
        balloon.update()
        balloon.draw()
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
