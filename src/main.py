import pygame, pytmx

from menu import build_menu

from configs import GAME_TITLE, DISPLAY_WIDTH, DISPLAY_HEIGHT


def main():

    pygame.init()

    display = pygame.display.set_mode(
        [DISPLAY_WIDTH, DISPLAY_HEIGHT]
    )
    
    pygame.display.set_caption(GAME_TITLE)

    build_menu(display)


if __name__ == "__main__":
    main()
