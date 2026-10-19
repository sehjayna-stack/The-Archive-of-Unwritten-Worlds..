import pygame
from gameMechanics.GamePiece import GamePiece

class Background():
    def __init__(self, image, x=0, y=0):
        self.image = image
        self.x = x
        self.y = y

        self.room = pygame.Surface(image.get_size())
        self.room.blit(image(0,0))

        self.pieces = []

    def addToBackground(self, image, x ,y):
        self.room.blit(image, (x, y))  # draws the provided image onto the background at the specified coordinates

    def addGamePiece(self, image, x, y, width=None, height=None): #interactable game piece that is part of the background
        piece = GamePiece(image, x, y, width, height)
        self.pieces.append(piece)

    def drawBackground(self, window, cameraX, cameraY):
        window.blit(self.room, (-cameraX, -cameraY))

        for piece in self.pieces:
            piece.draw(window, cameraX, cameraY)


