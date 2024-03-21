import sys
import pygame

from game import Game

from configs import BLACK, WHITE, RED, DISPLAY_WIDTH

# Função para desenhar o texto na tela
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Função para criar botões
def draw_button(text, font, color, surface, x, y, width, height):
    pygame.draw.rect(surface, color, (x, y, width, height))
    draw_text(text, font, BLACK, surface, x + width // 2, y + height // 2)

# Função principal do menu
def build_menu(display):
    font = pygame.font.Font(None, 36)
    menu = True

    while menu:
        display.fill(WHITE)
        draw_text('Menu Principal', font, BLACK, display, DISPLAY_WIDTH // 2, 100)
        
        # Desenhar os botões
        draw_button('Iniciar Jogo', font, RED, display, 300, 200, 200, 50)
        draw_button('Opções', font, RED, display, 300, 300, 200, 50)
        draw_button('Sair', font, RED, display, 300, 400, 200, 50)

        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 300 <= mouse_pos[0] <= 500 and 200 <= mouse_pos[1] <= 250:
                    print("Iniciar Jogo")
                    game = Game(display)
                    game.run()
                elif 300 <= mouse_pos[0] <= 500 and 300 <= mouse_pos[1] <= 350:
                    print("Opções")
                elif 300 <= mouse_pos[0] <= 500 and 400 <= mouse_pos[1] <= 450:
                    print("Quit")
                    menu = False
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
