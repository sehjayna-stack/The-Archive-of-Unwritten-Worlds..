import json

class readSpellsDatabase():

    def __init__(self, spellsDatabase):
        self.spellsDB = spellsDatabase
        with open("spellsDatabase.json") as f:#try this late: {spellsDB}
            data = json.load(f)

        self.spells = data["spells"]

    def findUsableSpells(self): #category must
        usableSpells = [
            (name, spell["marks"]["spellSequence"])
            for name, spell in self.spells.items()
                if spell["marks"]["usable"]
        ]
        return usableSpells

    def findMatchingSpell(self, letters, spells):
        usableSpells = self.findUsableSpells()

        return [
            name 
            for name, sequence in usableSpells
            if sequence in letters
        ]  