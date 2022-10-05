import random
import sys, os

from ..System.Util.GameObject import GameObject
from ..Data.GameData import GameData

from Script.Data.ColorList import ColorList
#sys.path.append('../../System/Util/')


# キャラの視界を設定マップへ反映するように追加

PLAYER = 0
ENEMY = 1


class Weapon(GameObject):
    def __init__(self):
        super.__init__()
        self.weaponName     = GameData.GetWeaponDataFromId().weaponName     # 武器名
        self.range          = GameData.GetWeaponDataFromId().range          # 射程距離
        self.power          = GameData.GetWeaponDataFromId().power          # 攻撃力
        self.actioncost    = GameData.GetWeaponDataFromId().actioncost    # 攻撃時の行動力消費
        self.angle          = GameData.GetWeaponDataFromId().angle          # 角度
        self.powerFlag      = GameData.GetWeaponDataFromId().powerFlag      # ユニットの攻撃力分を加算するかどうか
        self.plusdown       = GameData.GetWeaponDataFromId().plusdown       # 武器装備時の行動力の増減

