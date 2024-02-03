import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)
USER_WIDTH, USER_HEIGHT = 30,50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BOX Game")
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

def draw_USER(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, USER_WIDTH, USER_HEIGHT))

def draw_obstacle(obstacle):
    pygame.draw.rect(screen, RED, obstacle)

def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over():
    game_over_text = font.render("GAME Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds before closing the window
    pygame.quit()
    sys.exit()

def main():
    USER_x = WIDTH // 2 - USER_WIDTH // 2
    USER_y = HEIGHT - USER_HEIGHT - 10
    USER_speed = 5

    obstacle_speed = 5
    obstacles = []

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and USER_x > 0:
            USER_x -= USER_speed
        if keys[pygame.K_RIGHT] and USER_x < WIDTH - USER_WIDTH:
            USER_x += USER_speed

        # Move obstacles and spawn new ones
        for obstacle in obstacles:
            obstacle.y += obstacle_speed

        obstacles = [obstacle for obstacle in obstacles if obstacle.y < HEIGHT]

        if random.randint(1, 20) == 1:
            obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
            obstacle_y = -OBSTACLE_HEIGHT
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

        # Check for collisions
        USER_rect = pygame.Rect(USER_x, USER_y, USER_WIDTH, USER_HEIGHT)
        for obstacle in obstacles:
            if USER_rect.colliderect(obstacle):
                game_over()

        # Draw everything
        screen.fill((0, 0, 0))
        draw_USER(USER_x, USER_y)
        for obstacle in obstacles:
            draw_obstacle(obstacle)
        display_score(score)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

        score += 1

if __name__ == "__main__":
    main()
