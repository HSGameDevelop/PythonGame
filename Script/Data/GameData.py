import sys, os
sys.path.append('../../Script/Data/')

from Script.Data.CharacterData import CharacterDataLoader

class GameData:
    def LoadData(self):
        cdl = CharacterDataLoader()
        characterData = cdl.LoadData()
        print (characterData)

    characterData = []
