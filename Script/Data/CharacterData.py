import sys, os

sys.path.append('../../Script/Data/')
from Script.Data.DataBase import DataLoaderBase



class CharacterData:
    def __init__(self):
        self.characterId = 0    # キャラクターID
        self.characterName = '' # キャラクター名
        self.weaponId = 0       # 武器ID
        self.actionPower = 0    # 行動力
        self.skillSetId = 0     # スキルセットID       
    
class CharacterDataLoader(DataLoaderBase):
    LOAD_FILE_NAME = 'Character.bin'
    LOAD_FILE_PATH = DataLoaderBase.LOAD_BIN_FILE_DIRECTORY + LOAD_FILE_NAME

    # データの読みこみ
    def LoadCharacterData(self) -> CharacterData:
        return super().LoadData(self.LOAD_FILE_PATH, self.ConvertCharacterData)

    # キャラクターデータへの変換
    def ConvertCharacterData(self, data) -> CharacterData:
        characterDataList = []
        characterDataList = super().ConvertOutputData(data, characterDataList, self.CreateCharacterData)
        return characterDataList

    # キャラクターデータの作成
    def CreateCharacterData(self, data, columns)-> CharacterData:
        characterData = CharacterData()
        characterData = super().CreateOutputData(data, columns, characterData)
        return characterData




