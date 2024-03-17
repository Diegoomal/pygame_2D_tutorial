import pygame

from configs import BACKGROUND, RED, MAP_COLLISION_LAYER
from text import Text
from level import Level
from player import Player
from spritesheet import SpriteSheet


class Game:

    def __init__(self, screen):
        
        self.screen = screen

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
                        #print('resolution:', pygame.TIMER_RESOLUTION)
                        print('ticks:', pygame.time.get_ticks())
                        
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
        self.screen.fill(BACKGROUND)
        self.currentLevel.draw(self.screen)
        self.player.draw(self.screen)
        if self.debugging:
            self.screen.blit(self.overlay, [100, 100])

        self.text.draw(self.screen)
        self.text_fps.draw(self.screen)
        pygame.draw.rect(self.screen, RED, self.rect, 1)
        pygame.display.flip()

    def __str__(self):
        return f'{self.__class__.__name__} levels:{len(self.levels)}'
