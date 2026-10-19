'''
import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, x,y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height)) #creates an empty surface 
        self.image.fill(color)
        self.rect = self.image.get_rect() #draws a rect around the surface
        self.rect.center = (x, y) # gives the rect a position

crosshair = Crosshair(400, 300, 20, 20, (255, 0, 0)) #creates a crosshair object
crosshair_group = pygame.sprite.Group() #creates a group for the crosshair
crosshair_group.add(crosshair) #adds the crosshair to the group

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    crosshair_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

    sprite (surface -> rect) example 
'''