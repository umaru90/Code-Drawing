import pygame as Umaru 
import random
import math

Umaru.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CENTER_ATTRACTION_STRENGTH = 0.001
ATTRACTIVE_STRENGTH = 24
REPELLENT_STRENGTH = 36
MINIMUM_VELOCITY = 36
PARTICLE_RADIUS = 24

WHITE = (255, 255, 255)

screen = Umaru.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Umaru.display.set_caption("Particle System")

# Particle class
class Particle:
    def __init__(self, x, y, r):
        self.pos = Umaru.Vector2(x, y)
        self.vel = Umaru.Vector2()
        self.acc = Umaru.Vector2()
        self.r = r
        self.aStr = ATTRACTIVE_STRENGTH * r
        self.rStr = REPELLENT_STRENGTH * r
        self.col = WHITE

    def show(self):
        Umaru.draw.circle(screen, self.col, (int(self.pos.x), int(self.pos.y)), int(self.r))

    def update(self):
        self.vel += self.acc
        self.acc *= 0
        if self.vel.length() > MINIMUM_VELOCITY:
            self.vel.scale_to_length(MINIMUM_VELOCITY)
        self.pos += self.vel
        self.vel.scale_to_length(0.92)

        hue = Umaru.math.lerp(80, 0, 
        max(0, min(1, self.vel.length() / MINIMUM_VELOCITY)))  
        self.col = Umaru.Color(0)
        self.col.hsla = (hue, 100, 100, 100)

        dist = self.pos.distance_to(centerV)
        self.r = Umaru.math.lerp(PARTICLE_RADIUS, 0, max(0, min(1, dist / (SCREEN_WIDTH / 2))))  

    def updateForce(self, target):
        force = target.pos - self.pos
        d = force.length()
        force.normalize_ip()

        if d > 0.5:
            if d <= self.r * 8:
                fa = force * (self.aStr / (d * d))
                self.acc += fa
            if d <= self.r * 24:
                fs = force * (-self.rStr / (d * d))
                self.acc += fs
            if d < (self.r + target.r):
                mv = force * (d - (self.r + target.r))
                self.vel += mv * 0.5
                target.vel += mv * -0.5

    def updateMouse(self, mouse_x, mouse_y):
        mv = Umaru.Vector2(mouse_x, mouse_y)
        force = mv - self.pos
        d = force.length()
        force.normalize_ip()

        if d < MINIMUM_VELOCITY * 2:
            fs = force * -MINIMUM_VELOCITY
            self.acc += fs

# Create particles
particles = []
centerV = Umaru.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

for _ in range(600):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    particles.append(Particle(x, y, PARTICLE_RADIUS))

# Game loop
running = True
while running:
    for event in Umaru.event.get():
        if event.type == Umaru.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for p in particles:
        for target in particles:
            if p != target:
                p.updateForce(target)

        p.acc += (p.pos - centerV) * -CENTER_ATTRACTION_STRENGTH
        p.update()
        p.show()

    Umaru.display.flip()
Umaru.quit()
