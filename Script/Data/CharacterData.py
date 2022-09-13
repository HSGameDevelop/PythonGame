import sys, os
sys.path.append('../../System/IO/')
from ...System.IO.binaryFileManager import binaryFileManager

class CharacterDataLoader:
    LOAD_FILE_NAME = 'Character.bin'
    LOAD_FILE_PATH = __file__ + '/Resource/Bin/' + LOAD_FILE_NAME
    def LoadData(self):
        
        return

class CharacterData:
    characterId = 0
    characterName = ''
    weaponId = 0
    actionPower = 0
    skillSetId = 0

