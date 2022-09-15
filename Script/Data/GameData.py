import sys, os
sys.path.append('../../Script/Data/')

from Script.Data.CharacterData import CharacterData, CharacterDataLoader
from Script.Data.WeaponData import WeaponData, WeaponDataLoader

# ゲームのデータ関連を扱うクラス
class GameData:
    def __init__(self) -> None:
        characterData = []  # キャラクターデータ
        weaponData = []     # 武器データ

    # ゲームデータの読み込み
    def LoadData(self):
        # キャラクターデータの読み込み
        cdl = CharacterDataLoader()
        self.characterData = cdl.LoadCharacterData()

        # キャラクターデータの読み込み
        wdl = WeaponDataLoader()
        self.weaponData = wdl.LoadWeaponData()

    # キャラクターデータをIdから取得する
    def GetCharacterDataFromId(self, characterId) -> CharacterData:
        if self.characterData == None:
            return None 

        for data in self.characterData:
            if data.characterId == str(characterId):
                return data

        return None

    # 武器データをIdから取得する
    def GetWeaponDataFromId(self, weaponId) -> WeaponData:
        if self.weaponData == None:
            return None 

        for data in self.weaponData:
            if data.weaponId == str(weaponId):
                return data

        return None
