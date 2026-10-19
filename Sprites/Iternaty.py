import pygame  # pyright: ignore[reportMissingImports]
from Sprites.sprites import *

pygame.init()

class Iternaty(pygame.sprite.Sprite):
    #constructor: pass in the color 
    #and its x and y pos
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
    