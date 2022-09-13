import sys, os
sys.path.append('../../Script/Data/')

from Script.Data.CharacterData import CharacterDataLoader

class GameData:
    characterData = []  # キャラクターデータ

    def LoadData(self):
        # キャラクターデータの読み込み
        cdl = CharacterDataLoader()
        characterData = cdl.LoadData()
