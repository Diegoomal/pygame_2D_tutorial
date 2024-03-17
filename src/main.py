import pygame, pytmx

from configs import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE

from game import Game


def main():

    pygame.init()

    screen = pygame.display.set_mode(
        [SCREEN_WIDTH, SCREEN_HEIGHT]
    )
    
    pygame.display.set_caption(GAME_TITLE)

    game = Game(screen)
    game.run()


if __name__ == "__main__":
    main()
