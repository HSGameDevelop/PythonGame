import random
import sys, os

from ..System.Util.PgLib import PgLib
from ..System.Util.GameObject import GameObject
from ..Data.GameData import GameData

from Script.Data.ColorList import ColorList
#sys.path.append('../../System/Util/')


# キャラの視界を設定マップへ反映するように追加

PLAYER = 0
ENEMY = 1


class Weapon(GameObject):
    WEAPON_IMAGE_PATH = "Resource/Image/Battle/"
    IMAGE_SIZE = 128.0
    IMAGE_NUM_MAX = 15

    def __init__(self, id):
        super().__init__(size=(128,128))
        self.weaponId       = GameData.GetWeaponDataFromId(id).weaponId       # 武器ID
        self.weaponName     = GameData.GetWeaponDataFromId(id).weaponName     # 武器名
        self.weaponEnglish  =  self.English()                                  # 武器名(英語)
        self.range          = GameData.GetWeaponDataFromId(id).range          # 射程距離
        self.power          = GameData.GetWeaponDataFromId(id).power          # 攻撃力
        self.actioncost     = GameData.GetWeaponDataFromId(id).actioncost     # 攻撃時の行動力消費
        self.angle          = GameData.GetWeaponDataFromId(id).angle          # 角度
        self.powerFlag      = GameData.GetWeaponDataFromId(id).powerFlag      # ユニットの攻撃力分を加算するかどうか
        self.plusdown       = GameData.GetWeaponDataFromId(id).plusdown       # 武器装備時の行動力の増減
        self.isSelect = False

        self.image = PgLib.LoadImage(Weapon.WEAPON_IMAGE_PATH + self.weaponEnglish + ".png")

        self.SetSelect(self.isSelect)
        self.SetImage(self.image)
        self.SetBaseImage(self.image)
        self.SetAngle(0)

        

    def GetSelect(self):
        return self.isSelect

    def SetSelect(self, select):
        self.isSelect = select

    def Update(self):
        pass

    def English(self):
        if(self.weaponName == "こぶし"):
            return "Fist"
        if(self.weaponName == "爪"):
            return "Claw"
        if(self.weaponName == "剣"):
            return "Sword"
        if(self.weaponName == "両手剣"):
            return "Claymore"
        if(self.weaponName == "槍"):
            return "Spear"
        if(self.weaponName == "鎖鎌"):
            return "Sickle and Chain"
        if(self.weaponName == "クロスボウ"):
            return "Crossbow"
        if(self.weaponName == "マシンガン"):
            return "Machine Guns"
        if(self.weaponName == "長弓"):
            return "Longbow"
        if(self.weaponName == "スナイパー"):
            return "Sniper"
        if(self.weaponName == "ハンマー"):
            return "Hammer"
        if(self.weaponName == "まきびし"):
            return "Caltrop"
        if(self.weaponName == "トラバサミ"):
            return "Traversing scissors"
        if(self.weaponName == "爆弾"):
            return "Bomb"
        
