import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square Collision Simulation")

# Colors
BLACK = (0, 0, 0)
SQUARE_COLOR = (255, 0, 0)

class Square:
    def __init__(self, x, y, size, color, velocity):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.velocity = velocity

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (int(self.x), int(self.y), self.size, self.size))

    def check_bounds(self, width, height):
        # Collision with the left and right walls
        if self.x <= 0 or self.x + self.size >= width:
            self.velocity[0] *= -1  # Reverse horizontal velocity

        # Collision with the top and bottom walls
        if self.y <= 0 or self.y + self.size >= height:
            self.velocity[1] *= -1  # Reverse vertical velocity

    def check_square_collision(self, other_square):
        # Check for collision with another square (simple bounding box check)
        if (self.x < other_square.x + other_square.size and
            self.x + self.size > other_square.x and
            self.y < other_square.y + other_square.size and
            self.y + self.size > other_square.y):
            # Reverse velocities upon collision
            self.velocity[0] *= -1
            self.velocity[1] *= -1
            other_square.velocity[0] *= -1
            other_square.velocity[1] *= -1

# Initialize squares with size 15
squares = []
square_size = 15
for _ in range(100):
    x = random.randint(50, WIDTH - square_size)
    y = random.randint(50, HEIGHT - square_size)
    color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    velocity = [random.uniform(-3, 3), random.uniform(-3, 3)]  # Random velocity for movement
    squares.append(Square(x, y, square_size, color, velocity))

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move squares, check bounds, and check for collisions with other squares
    for i, square in enumerate(squares):
        square.move()
        square.check_bounds(WIDTH, HEIGHT)

        # Check for collision with other squares
        for j, other_square in enumerate(squares):
            if i != j:
                square.check_square_collision(other_square)

        square.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
