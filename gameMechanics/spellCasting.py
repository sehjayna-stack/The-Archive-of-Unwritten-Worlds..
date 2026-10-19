import pygame
#from SaveFiles.editSave import SaveFile
pygame.init()
#from readSpellsDatabase import readSpellsDatabase 

#global spellDB; spellDB = readSpellsDatabase()

'''
Spellcasting class: implements the spell-casting game mechanic
    .readKeys(key, list) -> reads the last 5 - 7 keys that user inputs and returns them
    .displayLettersInterface.store() -> display read letters (readKeys) for the user, also stores them in a list 
    .displayLettersInterface.update() -> pushes the previously typed letters to the left, once list is 8 letters long, delete the first letter. 
    .displayLettersInterface.kill() -> kills the interface
    .displayLettersInterface.restrict() -> restrict the use of certain spells
    .displayLettersInterface.isolate(spellName) -> finds the value and index number of the letters that match a spell. 

    .findSpell ->  finds a spell that the user knows or find a spell when searched for
    .implementSpell -> initiates spell consequences and animation
    
    .glow() -> lights up the displayLettersInterface
'''


class SpellCastingMechanic(): #create outside of the game loop
    def __init__(self, screen):
        #load the testbase image,
    
        self.letters = ""; self.state = "closed"
        self.font = pygame.font.Font(None, 60) #creates font
        self.screen = screen
        self.textSurface = self.font.render(self.letters, True, (255,255,255))


    def wait(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.state = "open"                

    def open(self, event): #use this in the game loop after the window and background  are drawnand before pygame.display.update
        if event.type == pygame.KEYDOWN: # type: ignore
            if event.unicode.isalpha() and event.unicode.islower(): # type: ignore
                self.letters += event.unicode # type: ignore
                if len(self.letters) > 7:
                    self.letters = self.letters[1:]
            elif event.key == pygame.K_RETURN:
                self.letters = ""
                self.state = "closed"
            else: pass
        else: pass

        self.textSurface = self.font.render(self.letters, True, (255,255,255))
        

    def castSpell(self):
        matches = []

        for name, spell in self.spells.items():
            if spell["marks"]["usable"]:
                seq = spell["marks"]["spellSequence"]
                if seq in self.letters:
                    matches.append(name)

        if matches: 
            self.textSurface = self.font.render(self.letters, True, (255,0,0))
        else: self.textSurface = self.font.render(self.letters, True, (255,255,255))




    def drawLetters(self):
        self.screen.blit(self.textSurface, (50, 50))

    



