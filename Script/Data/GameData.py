import sys, os
sys.path.append('../../Script/Data/')

from Script.Data.CharacterData import CharacterData, CharacterDataLoader
from Script.Data.WeaponData import WeaponData, WeaponDataLoader

sys.path.append('../System/Util/')
from ..System.Util.Singleton import Singleton

# ゲームのデータ関連を扱うクラス
class GameDataImpl(Singleton):
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

# ゲームのデータ関連を扱うクラス(呼び出し側)
gameData : GameDataImpl = None
class GameData:
    # 初期化
    @staticmethod
    def Initialize():
        global gameData
        gameData = GameDataImpl()

    # インスタンス取得
    @staticmethod
    def GetInstance() -> GameDataImpl:
        if gameData == None:
            GameData.Initialize()
        return gameData;

    # ゲームデータの読み込み
    @staticmethod
    def LoadData():
        GameData.GetInstance().LoadData()

    # キャラクターデータをIdから取得する
    @staticmethod
    def GetCharacterDataFromId(characterId) -> CharacterData:
        return GameData.GetInstance().GetCharacterDataFromId(characterId)

    # 武器データをIdから取得する
    @staticmethod
    def GetWeaponDataFromId(weaponId) -> WeaponData:
        return GameData.GetInstance().GetWeaponDataFromId(weaponId)
