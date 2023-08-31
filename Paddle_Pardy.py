import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 130, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Paddle Party")
clock = pygame.time.Clock()

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 60
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= self.speed
        elif direction == "down" and self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 8
        self.speed_x = random.choice([-4, 4])
        self.speed_y = random.choice([-4, 4])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Ball collision with top and bottom
        if self.y <= 0 or self.y >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)

def main():
    paddle_left = Paddle(5, SCREEN_HEIGHT // 2 - 30)
    paddle_right = Paddle(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - 30)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle_right.move("up")
        if keys[pygame.K_DOWN]:
            paddle_right.move("down")
        if keys[pygame.K_w]:
            paddle_left.move("up")
        if keys[pygame.K_s]:
            paddle_left.move("down")

        ball.move()

        # Ball collision with paddles
        if ball.x - ball.radius <= paddle_left.x + paddle_left.width and ball.y >= paddle_left.y and ball.y <= paddle_left.y + paddle_left.height or \
           ball.x + ball.radius >= paddle_right.x and ball.y >= paddle_right.y and ball.y <= paddle_right.y + paddle_right.height:
            ball.speed_x = -ball.speed_x

        paddle_left.draw()
        paddle_right.draw()
        ball.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()