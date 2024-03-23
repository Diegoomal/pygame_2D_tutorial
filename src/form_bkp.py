import sys
import pygame

from game import Game

from configs import BLACK, WHITE, RED, DISPLAY_WIDTH, DISPLAY_HEIGHT


class FormMenuItem:
    
    def __init__(
            self,
            element_type = 'title',
            element_text = 'title',
            pos=(0, 0),
            size=(0, 0)
        ):
        self.element_type=element_type
        self.element_text=element_text
        self.pos=pos
        self.size=size


class FormMenu:

    def __init__(self, display, is_running = True):
        self.display = display
        self.is_running = True
        self.menu_itens = []
        self.font = pygame.font.Font(None, 36)
    
    def set_running(self, is_running):
        self.is_running
    
    def update_running(self):
        self.is_running = not self.is_running

    def set_title(self, title):
        self.set_title = title

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    def draw_button(self, text, font, color, surface, x, y, width, height):
        pygame.draw.rect(surface, color, (x, y, width, height))
        self.draw_text(text, font, BLACK, surface, x + width // 2, y + height // 2)

    def add_item(self, element_type, element_text, pos=(0, 0), size=(0, 0)):
        item = FormMenuItem(element_type, element_text, pos, size)
        self.menu_itens.append(item)

    def draw_elements(self):
        self.display.fill(WHITE)
        # self.draw_text('Menu Principal', self.font, BLACK, self.display, DISPLAY_WIDTH // 2, 100)
        # self.draw_button('Iniciar Jogo', self.font, RED, self.display, 250, 200, 200, 50)
        # self.draw_button('Opções', self.font, RED, self.display, 250, 300, 200, 50)
        # self.draw_button('Sair', self.font, RED, self.display, 250, 400, 200, 50)
        for item in self.menu_itens:
            if item.element_type == 'LABEL':
                self.draw_text(
                    item.element_text, 
                    self.font,
                    RED,
                    self.display,
                    item.pos[0],
                    item.pos[1]
                )
            elif item.element_type == 'BUTTON':
                self.draw_button(
                    item.element_text, 
                    self.font,
                    RED,
                    self.display,
                    item.pos[0], item.pos[1],
                    item.size[0], item.size[1]
                )

    def build(self):
        
        self.draw_elements()
    
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 300 <= mouse_pos[0] <= 500 and 200 <= mouse_pos[1] <= 250:
                        print("Iniciar Jogo")
                        game = Game(self.display)
                        game.run()
                    elif 300 <= mouse_pos[0] <= 500 and 300 <= mouse_pos[1] <= 350:
                        print("Opções")
                    elif 300 <= mouse_pos[0] <= 500 and 400 <= mouse_pos[1] <= 450:
                        print("Quit")
                        menu = False
                        pygame.quit()
                        sys.exit()
            pygame.display.update()