
import pygame
from config import *
from Sprites import *
from SaveFiles.editSave import *
from gameMechanics.spellCasting import SpellCastingMechanic
from Sprites.player import Player
import asyncio

pygame.init()

global gameState
global player; player = Player()
global saveFile; saveFile = SaveFile('save.json')

class Window:
    def __init__(self, gameState):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock() #creates a clock object to control the frame rate
        #self.font = pygame.font.Font("Arial", 30) 
        self.running = True
        self.gameState = gameState

        self.cameraX = 0
        self.cameraY = 0

    def run(self):

        async def main():
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if spellCastingInterface.state == "closed":
                        spellCastingInterface.wait(event)
                    elif spellCastingInterface.state == "open":
                        spellCastingInterface.open(event)
                    # spellCastingInterface.castSpell()

                self.window.fill((0, 0, 0))  # fill screen with black




                player.update()
                player.draw(screen.window, self.cameraX, self.cameraY)

                spellCastingInterface.drawLetters()

                pygame.display.update()
                self.clock.tick(60)          #limit framerate to 60 fps 
                await asyncio.sleep(0)

        asyncio.run(main())



    def drawSurface(self, background):
        self.window.blit(background, (0, 0))  # draw the background image

    def updateGamestate(self, gameState):
        # Update the game state here
        self.gameState = gameState        

    
if __name__ == "__main__":
    screen = Window(None)
    global spellCastingInterface; spellCastingInterface = SpellCastingMechanic(screen.window)


    screen.run()

