import pygame
from config import *
import math
import random

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, image=None):
        #calls the Sprite constructor first
        super().__init__()

        self.image = pygame.Surface((50,50))
        self.image.fill(((0,255,0))) #temp green player sprite.
        #self.image = pygame.image.load("player.png").convert alpha 

        #creates hitbox area of the image
        self.rect = self.image.get_rect(center = (400,300))
        self.rect.center = (400,300)

        #define speed
        self.speed = 5

    def update(self):
        #"handles player movement based on keyboar input"
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: 
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, surface, cameraX, cameraY):
        surface.blit(self.image, (self.rect.x - cameraX, self.rect.y - cameraY))


