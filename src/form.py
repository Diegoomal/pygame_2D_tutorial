import sys
import pygame
from abc import ABC, abstractmethod
from game import Game
from configs import BLACK, WHITE, RED, DISPLAY_WIDTH, DISPLAY_HEIGHT


class FormMenuItem:
    def __init__(
            self,
            type,
            text,
            pos,
            size,
            color,
            font,
    ):
        self.type = type
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.font = pygame.font.Font(None, 36) if font is None else font


class FormMenu():

    def __init__(self, display, is_running=True):
        self.display = display
        self.is_running = True
        self.menu_items = []
        self.font = pygame.font.Font(None, 36)

    def set_running(self, is_running):
        self.is_running

    def update_running(self):
        self.is_running = not self.is_running
    
    def draw_text(self, fmi: FormMenuItem):
        surface = self.display
        text, font, color, x, y = fmi.text, fmi.font, fmi.color, fmi.pos[0], fmi.pos[1]
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    def draw_button(self, fmi: FormMenuItem):
        
        surface = self.display
        text, font, color, x, y, width, height = fmi.text, fmi.font, fmi.color, fmi.pos[0], fmi.pos[1], fmi.size[0], fmi.size[1]
        
        pygame.draw.rect(surface, color, (x, y, width, height))
        
        new_pos = (x + width // 2, y + height // 2)
        fmi2 = FormMenuItem(fmi.type, fmi.text, new_pos, fmi.size, BLACK, fmi.font)
        self.draw_text(fmi2)

    def add_item(self, element_type, element_text, pos, size, color, font):
        item = FormMenuItem(element_type, element_text, pos, size, color, font)
        self.menu_items.append(item)       

    def build(self):
        
        self.display.fill(WHITE)
        for item in self.menu_items:
            if item.type == 'LABEL':
                self.draw_text(item)
            elif item.type == 'BUTTON':
                self.draw_button(item)

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
