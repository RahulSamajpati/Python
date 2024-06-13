import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set the circle properties
CIRCLE_CENTER = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
CIRCLE_RADIUS = 200

# Set the ball properties
BALL_RADIUS = 10
BALLS_COUNT = 5  # Number of balls

# Initialize the screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bouncing Balls in a Circle")

# Initialize the clock
clock = pygame.time.Clock()

# Ball class to handle the ball's position and movement
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = random.uniform(-5, 5)  # Random initial x velocity
        self.dy = random.uniform(-5, 5)  # Random initial y velocity

    def move(self):
        # Move the ball
        self.x += self.dx
        self.y += self.dy

        # Check for collision with the circle's boundary
        distance_from_center = math.sqrt((self.x - CIRCLE_CENTER[0]) ** 2 + (self.y - CIRCLE_CENTER[1]) ** 2)
        if distance_from_center + self.radius > CIRCLE_RADIUS:
            # Change color on bounce
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            # Calculate the angle of incidence
            normal_vector = (self.x - CIRCLE_CENTER[0], self.y - CIRCLE_CENTER[1])
            normal_length = math.sqrt(normal_vector[0] ** 2 + normal_vector[1] ** 2)
            normal_unit = (normal_vector[0] / normal_length, normal_vector[1] / normal_length)

            # Reflect the velocity vector
            dot_product = self.dx * normal_unit[0] + self.dy * normal_unit[1]
            self.dx -= 2 * dot_product * normal_unit[0]
            self.dy -= 2 * dot_product * normal_unit[1]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def main():
    balls = [Ball(CIRCLE_CENTER[0], CIRCLE_CENTER[1], BALL_RADIUS, RED) for _ in range(BALLS_COUNT)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move each ball
        for ball in balls:
            ball.move()

        # Clear the screen
        screen.fill(BLACK)

        # Draw the circle
        pygame.draw.circle(screen, WHITE, CIRCLE_CENTER, CIRCLE_RADIUS, 2)

        # Draw each ball
        for ball in balls:
            ball.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
