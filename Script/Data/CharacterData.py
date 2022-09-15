import sys, os
sys.path.append('../System/IO/')
from ..System.IO.BinaryFileManager import BinaryFileManager

class CharacterData:
    def __init__(self):
        self.characterId = 0    # キャラクターID
        self.characterName = '' # キャラクター名
        self.weaponId = 0       # 武器ID
        self.actionPower = 0    # 行動力
        self.skillSetId = 0     # スキルセットID       
    
class CharacterDataLoader:
    LOAD_FILE_NAME = 'Character.bin'
    LOAD_FILE_PATH = os.getcwd() + '/Resource/Bin/' + LOAD_FILE_NAME

    # データの読みこみ
    def LoadData(self):
        bfm = BinaryFileManager()
        data = bfm.ReadFileToString(self.LOAD_FILE_PATH)
        return self.ConvertCharacterData(data)

    # キャラクターデータへの変換
    def ConvertCharacterData(self, data):
        characterDataList = []
        convertData = data.splitlines()
        columns = convertData[0].split(',') # 先頭行はパラメータ名

        for i in range(len(convertData)):
            if i == 0: # 先頭行はパラメータ名の為、弾く
                continue
            characterDataList.append(self.CreateCharacterData(convertData[i], columns))
        return characterDataList

    # キャラクターデータの作成
    def CreateCharacterData(self, data, columns)-> CharacterData:
        characterData = CharacterData()
        keys = list(characterData.__dict__.keys()) 
        params = data.split(',')

        for i in range(len(params)):
            for j in range(len(keys)):
                if keys[j].lower() == columns[i].lower():
                    characterData.__setattr__(keys[j], params[i]) 
                    break

        return characterData




