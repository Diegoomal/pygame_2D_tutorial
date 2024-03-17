import pygame

#Sprit sheet class to load sprites from player spritesheet
class SpriteSheet:
    def __init__(self, file_name, tile_size):
        self.file_name = file_name
        self.tile_size = tile_size
        self.sheet = pygame.image.load(file_name)
        self.rect = self.sheet.get_rect()
        print(self)

    def image_at(self, x, y):
        w, h = self.tile_size
        pos = w * x, h * y
        image = pygame.Surface(self.tile_size, pygame.SRCALPHA, 32).convert_alpha()
        image.blit(self.sheet, (0, 0), (pos, self.tile_size))
        return image

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file_name} size:{self.rect.size} tile:{self.tile_size}'
