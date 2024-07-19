import pygame
from page import Page


class Menu(Page):
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)  # تم تصغير حجم الخط إلى 48
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'exit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'game'

            self.screen.fill((0, 0, 0))
            text = self.font.render('Press Enter to Start', True, (255, 255, 255))
            text_sound = self.font.render('Turn on the sound to hear the eating sound', True, (255, 255, 255))

            text_rect = text.get_rect(center=(self.screen.get_width() // 2, 250))
            text_sound_rect = text_sound.get_rect(center=(self.screen.get_width() // 2, 300))

            self.screen.blit(text, text_rect)
            self.screen.blit(text_sound, text_sound_rect)

            pygame.display.flip()
            self.clock.tick(60)
