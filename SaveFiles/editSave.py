'''
Game class: holds features that changes anything
    .change.Act(actName) -> act      changes act
    .change.Scene(sceneNumber) -> scene  changes scene

    .change.gameBackground(newBackground) -> background    changes background
    .change.gamestate(newGamestate) -> battle, roleplay, teach
    .change.context() -> context so specific spells are casted the way the user probably wanted
    .add.context() -> adds new pieces of context, writes them at the end of a the context list of the spells.
    .savelearnedSpells() -> saves spells learned
    .saveInventory() -> saves what's in your inventory
    .saveGeneralContext() -> saves information that regards to the general context
    .saveSpellInformation() -> saves details about your spells
    .saveBackgroundDetails() -> saves what goes into the background 
    .

'''

import json

class SaveFile():
    def __init__(self, saveFile):
        self.saveFile = saveFile

    def writeFile(self, data):
        with open(self.saveFile, "w") as f:
            json.dump(data, f, indent = 4)
        return "fileSaved"

    def readFile(self):
        try:
            with open(self.saveFile, "r") as f:
                return json.load(f)
        except: return None
    

    def save_gameState(self, act=None, scene=None):
        data = self.readFile() or {}
        data ["gameState"] = {
                "act": act,
                "scene": scene
            }
        
        self.writeFile(data)

    def save_game(self, player, camera_x, camera_y):
        data = self.readFile() or {}

        data["player"] = {
                "x": player.world_x,
                "y": player.world_y
            },
            
        data["camera"]={
                "x": camera_x,
                "y": camera_y
            }

        self.writeFile(data)
    '''
    def save_learnedSpells(self, newSpells):
        data = self.readFile() or {}

        data["Spells"] = {
            "spells learned": []
        }
    '''

        
    '''
            "background":{
                "backgroundInUse": background
            } #research if you can remove images from background; if yes, add this to camera, if no, keep
        '''     
    
        
        
