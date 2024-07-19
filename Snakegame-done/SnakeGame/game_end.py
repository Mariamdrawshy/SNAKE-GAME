import pygame
from page import Page


class GameEnd(Page):
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'exit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'game'
                    if event.key == pygame.K_ESCAPE:
                        return 'menu'

            self.screen.fill((0, 0, 0))
            text = self.font.render('Game Over! Press Enter to Restart', True, (255, 255, 255))
            self.screen.blit(text, (50, 250))

            pygame.display.flip()
            self.clock.tick(60)
