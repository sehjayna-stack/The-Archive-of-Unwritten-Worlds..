import pygame

class GamePiece:
    def __init__ (self, image, x, y, width=None, height=None):

        if width and height:
            self.image = pygame.transform.scale(image, (width, height))
        else:
            self.image = image

        self.rect = self.image.get_rect(topleft = (x,y))

    def draw(self, surface, cameraX, cameraY):
        surface.blit(self.image, (self.rect.x - cameraX, self.y - cameraY))