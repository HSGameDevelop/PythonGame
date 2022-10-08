import sys, os

from .DataBase import DataLoaderBase

class CharacterData:
    def __init__(self):
        self.characterId = 0    # キャラクターID
        self.characterName = '' # キャラクター名
        self.actionpower = 0    # 行動力
        self.hitpoint = 0       # HP
        self.attackpoint = 0    # 攻撃力
        self.defensepoint = 0   # 防御力
        self.avoidancepoint = 0 # 回避力
        self.technologypoint = 0# 技術力
        self.visible = 0        # 視界
    
class CharacterDataLoader(DataLoaderBase):
    LOAD_FILE_NAME = 'Character.bin'
    LOAD_FILE_PATH = DataLoaderBase.LOAD_BIN_FILE_DIRECTORY + LOAD_FILE_NAME

    # キャラクターデータの読みこみ
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
