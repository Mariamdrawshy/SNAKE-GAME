import pygame
from menu import Menu
from game import Game
from game_end import GameEnd


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snake Game')

    menu = Menu(screen)
    game = Game(screen)
    game_end = GameEnd(screen)

    current_page = 'menu'

    while True:
        if current_page == 'menu':
            current_page = menu.run()
        elif current_page == 'game':
            current_page = game.run()
        elif current_page == 'game_end':
            current_page = game_end.run()
        elif current_page == 'exit':
            break

    pygame.quit()


if __name__ == '__main__':
    main()
