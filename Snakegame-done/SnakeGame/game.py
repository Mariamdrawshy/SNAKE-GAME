import pygame
import random

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load('background.png')
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.snake = [(100, 50), (90, 50), (80, 50)]
        self.direction = pygame.K_RIGHT
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False

        self.snake_speed = 15

        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        # Load the sound
        self.eat_sound = pygame.mixer.Sound('eat_sound.wav')

    def generate_food(self):
        return (random.randint(1, 79) * 10, random.randint(1, 59) * 10)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                        self.direction = event.key
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_r and self.game_over:
                        self.restart_game()

            if not self.game_over:
                self.move_snake()
                if self.check_collision():
                    self.game_over = True
                self.check_food()

            self.screen.blit(self.background, (0, 0))

            if self.game_over:
                self.show_game_over()
            else:
                self.draw_snake()
                self.draw_food()
                self.show_score()

            pygame.display.flip()
            self.clock.tick(self.snake_speed)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == pygame.K_LEFT:
            head_x -= 10
        elif self.direction == pygame.K_RIGHT:
            head_x += 10
        elif self.direction == pygame.K_UP:
            head_y -= 10
        elif self.direction == pygame.K_DOWN:
            head_y += 10

        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        head = self.snake[0]
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            return True
        if head in self.snake[1:]:
            return True
        return False

    def check_food(self):
        if self.snake[0] == self.food:
            self.eat_sound.play()  # Play sound when snake eats food
            self.food = self.generate_food()
            self.snake.append(self.snake[-1])
            self.score += 10

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, (*segment, 10, 10))

    def draw_food(self):
        pygame.draw.rect(self.screen, RED, (*self.food, 10, 10))

    def show_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def show_game_over(self):
        game_over_text = self.font.render("Game Over", True, WHITE)
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        restart_text = self.small_font.render("Press R to restart", True, WHITE)

        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 250))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 300))
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 350))

    def restart_game(self):
        self.snake = [(100, 50), (90, 50), (80, 50)]
        self.direction = pygame.K_RIGHT
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    show_start_screen(screen)

    game = Game(screen)
    game.run()

    pygame.quit()

def show_start_screen(screen):
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

    welcome_text = font.render("Welcome to Snake Game!", True, WHITE)
    start_text = small_font.render("Press Enter to start", True, WHITE)

    screen.blit(welcome_text, (SCREEN_WIDTH // 2 - welcome_text.get_width() // 2, 250))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 300))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

if __name__ == '__main__':
    main()
