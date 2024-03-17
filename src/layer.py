import pygame

from tile import Tile

class Layer:
    def __init__(self, index, mapObject):
        #Layer index from tiled map
        self.index = index
        
        #Create gruop of tiles for this layer
        self.tiles = pygame.sprite.Group()
        
        #Reference map object
        self.mapObject = mapObject
        
        #Create tiles in the right position for each layer
        for x in range(self.mapObject.width):
            for y in range(self.mapObject.height):
                img = self.mapObject.get_tile_image(x, y, self.index)
                if img:
                    tile = Tile(img, x * self.mapObject.tilewidth, y * self.mapObject.tileheight)
                    self.tiles.add(tile)
        print(self)

    #Draw layer
    def draw(self, screen):
        self.tiles.draw(screen)

    def __str__(self):
        return f'{self.__class__.__name__} index:{self.index} tiles:{len(self.tiles)}'
