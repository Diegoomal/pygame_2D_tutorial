import sys
import pygame

from text import Text
from level import Level
from player import Player
from spritesheet import SpriteSheet
from configs import BACKGROUND, RED, MAP_COLLISION_LAYER
from configs import BLACK, WHITE, RED, DISPLAY_WIDTH, DISPLAY_HEIGHT


class Game:

    def __init__(self, display):
        
        self.display = display

        #Set up a level to load
        self.currentLevelNumber = 0
        self.levels = []
        self.levels.append(Level(fileName = "resources/level1.tmx"))
        self.currentLevel = self.levels[self.currentLevelNumber]
        
        #Create a player object and set the level it is in
        self.player = Player(200, 100)
        self.player.currentLevel = self.currentLevel
        
        #Draw aesthetic overlay
        self.overlay = pygame.image.load("resources/overlay.png")
        self.clock = pygame.time.Clock()
        self.running = True
        self.debugging = False
        self.text = Text('game')
        self.text_fps = Text('fps', (0, 24))
        self.rect = pygame.Rect(10, 10, 100, 100)
        print(self)

    def run(self):
        
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.debugging = not self.debugging
                        print(f'debug: {self.debugging}')
                    elif event.key == pygame.K_t:
                        print('ticks:', pygame.time.get_ticks())
                    elif event.key == pygame.K_ESCAPE:
                        print('ESC pressed')
                        self.pause_game()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.key.get_mods() & 256:
                        self.player.rect.center = event.pos
                    else:
                        self.rect.topleft = event.pos
                        group = self.currentLevel.layers[MAP_COLLISION_LAYER].tiles
                        hits = pygame.sprite.spritecollide(self, group, False)
                        for hit in hits:
                            print(hit.__class__.__name__, hit.rect)

                self.player.do_event(event)

            self.text.render(f'ticks:{pygame.time.get_ticks()}')
            self.text_fps.render(f'fps:{self.clock.get_fps():.2f}')

            self.player.update()
            self.draw()
            self.clock.tick(60) 

        pygame.quit()

    def draw(self):
        self.display.fill(BACKGROUND)
        self.currentLevel.draw(self.display)
        self.player.draw(self.display)
        if self.debugging:
            self.display.blit(self.overlay, [100, 100])

        self.text.draw(self.display)
        self.text_fps.draw(self.display)
        pygame.draw.rect(self.display, RED, self.rect, 1)
        pygame.display.flip()

    def __str__(self):
        return f'{self.__class__.__name__} levels:{len(self.levels)}'





    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    def draw_button(self, text, font, color, surface, x, y, width, height):
        pygame.draw.rect(surface, color, (x, y, width, height))
        self.draw_text(text, font, BLACK, surface, x + width // 2, y + height // 2)

    def pause_game(self):
        font = pygame.font.Font(None, 36)
        self.draw_text('PAUSE', font, BLACK, self.display, DISPLAY_WIDTH // 2, 100)
        self.draw_button('Continuar', font, RED, self.display, 250, 200, 200, 50)
        self.draw_button('Sair', font, RED, self.display, 250, 300, 200, 50)
        self.display.fill((255, 0, 0, 50), special_flags=pygame.BLEND_RGBA_MULT)
    
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 300 <= mouse_pos[0] <= 500 and 200 <= mouse_pos[1] <= 250:
                        print('continue')
                        is_paused = False
                    elif 300 <= mouse_pos[0] <= 500 and 300 <= mouse_pos[1] <= 350:
                        print("Quit")
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            self.clock.tick(60)
