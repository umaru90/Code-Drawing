import pygame
import random

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matrix4_code_rain")

font = pygame.font.SysFont("ms mincho", 25)

matrix_code = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;':\",./<>?"

matrix_code_rain = []

for i in range(0, 800):
    matrix_code_rain.append([random.randint(0, height), random.randint(0, width), random.randint(0, len(matrix_code) - 1)])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    for i in range(0, len(matrix_code_rain)):
        rain_drop = matrix_code_rain[i]
        text = font.render(matrix_code[rain_drop[2]], True, (0, 255, 0))
        screen.blit(text, (rain_drop[1], rain_drop[0]))
        rain_drop[0] += 10

        if rain_drop[0] > height:
            rain_drop[0] = random.randint(-200, -50)
            rain_drop[1] = random.randint(0, width)

    pygame.display.update()
