import pygame, pytmx

from menu import build_menu

from configs import GAME_TITLE, DISPLAY_WIDTH, DISPLAY_HEIGHT, BLACK, WHITE, RED

from form import FormMenu, FormMenuItem


def main():

    pygame.init()

    display = pygame.display.set_mode(
        [DISPLAY_WIDTH, DISPLAY_HEIGHT]
    )
    
    pygame.display.set_caption(GAME_TITLE)

    # build_menu(display)

    menu = FormMenu(display, True)
    menu.add_item('LABEL', 'MENU', (DISPLAY_WIDTH // 2, 100), (0, 0), BLACK, None)
    menu.add_item('BUTTON', 'INICIAR', (250, 200), (200, 50), RED, None)
    menu.add_item('BUTTON', 'OPCOES', (250, 300), (200, 50), RED, None)
    menu.add_item('BUTTON', 'SAIR', (250, 400), (200, 50), RED, None)
    menu.build()


if __name__ == "__main__":
    main()
