import pygame

class Text:

    def __init__(self, text, pos=(0, 0)):
        self.font = pygame.font.Font(None, 24)
        self.color = (255, 255, 255)
        self.text = text
        self.pos = pos
        self.render(text)

    def render(self, text):
        self.image = self.font.render(text, 1, self.color)

    def draw(self, screen):
        screen.blit(self.image, self.pos)
