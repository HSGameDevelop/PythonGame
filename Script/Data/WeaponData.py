import sys, os

sys.path.append('../../Script/Data/')
from Script.Data.DataBase import DataLoaderBase

class WeaponData:
    def __init__(self):
        self.weaponId = 0       # 武器ID
        self.weaponName = ''    # 武器名
        self.range = 0          # 射程距離
        self.power = 0          # 攻撃力
        self.consumption = 0    # 攻撃時の行動力消費
        self.powerFlag = 0      # ユニットの攻撃力分を加算するかどうか
        self.plusdown = 0       # 武器装備時の行動力の増減
    
class WeaponDataLoader(DataLoaderBase):
    LOAD_FILE_NAME = 'Weapon.bin'
    LOAD_FILE_PATH = DataLoaderBase.LOAD_BIN_FILE_DIRECTORY + LOAD_FILE_NAME

    # 武器データの読みこみ
    def LoadWeaponData(self) -> WeaponData:
        return super().LoadData(self.LOAD_FILE_PATH, self.ConvertWeaponData)

    # 武器データへの変換
    def ConvertWeaponData(self, data) -> WeaponData:
        weaponDataList = []
        weaponDataList = super().ConvertOutputData(data, weaponDataList, self.CreateWeaponData)
        return weaponDataList

    # 武器データの作成
    def CreateWeaponData(self, data, columns)-> WeaponData:
        weaponData = WeaponData()
        weaponData = super().CreateOutputData(data, columns, weaponData)
        return weaponData
