import random
import sys, os

from ...Util.GameObject import GameObject
from ..Data.GameData import GameData
from ..Data.ColorList import ColorList
from .CharacterStatus import CharacterStatus
from .BattleDefine import *

# キャラの視界を設定マップへ反映するように追加

h_w = 50.15
h_w1_4 = h_w / 4
h_w1_2 = h_w / 2
h_w3_4 = h_w * (3 / 4)

h_h = 57.3
h_h3_4 = h_h * (3 / 4)
h_h1_4 = h_h / 4
h_h1_2 = h_h / 2


class CharacterManager():
    def __init__(self, xi, xj, yi, yj, num):
         # ユニットが同じ位置に生成されないように確認
        while True:
            xl = self.rand_ints_x(xi, xj, num)
            yl = self.rand_ints_y(yi, yj, num)
            z = self.rand_ints_check(xl, yl, num)
            if z == True:
                break
        self.xl = xl
        self.yl = yl

        #  player 重複なし
    def rand_ints_x(self, i, j, num):
        xl = []
        while len(xl) < num:
            x = random.randint(i, j)
            xl.append(x)
        return xl

    def rand_ints_y(self, i, j, num):
        yl = []
        while len(yl) < num:
            y = random.randint(i, j)
            yl.append(y)
        return yl

    def rand_ints_check(self, xl, yl, num):
        for x in range(num):
            for y in range(num):
                if xl[x] == xl[y] and x != y:
                    if yl[x] == yl[y] and x != y:
                        return False
        return True


class Character(GameObject):
    def __init__(self, xl, yl, side, num):
        super().__init__()
        self.unit_side = side
        self.__isSelect = False
        self.__isVisible = False

        self.xl, self.yl, self.x, self.y, self.tagname = self.prepareUnit(xl, yl)
        self.ID = num
        if self.unit_side == SideType.Player:
            self.chara = random.randint(CharacterNum.PlayerStart, CharacterNum.PlayerMax)  # excelのプレイヤーの種類
        else:
            self.chara = random.randint(CharacterNum.EnemyStart, CharacterNum.EnemyMax) # excelのエネミーの種類
        
        characterData = GameData.GetCharacterDataFromId(self.chara)
        self.__status : CharacterStatus = CharacterStatus(characterData) # ステータス

        self.__weaponId = None
        self.__secondWeaponId = None

        self.armorId = None


    def prepareUnit(self, xl, yl):
        # (x,y)のマスの中心座標を計算
        #self.xy = []
        if yl % 2 == 0:
            x = h_w * xl
            y = h_h3_4 * yl - h_h1_4
            #self.SetPos(x, y)
        elif yl % 2 == 1:
            x = h_w1_2 + (xl * h_w)
            y = (h_h3_4 * yl) - h_h1_4
            #self.SetPos(x, y)
        
        # (x, y)座標
        tagname = "(" + str(xl) + "," + str(yl) + ")"
        #self.xy.append([id, xl, yl, x, y, tagname])
        return xl, yl, x, y, tagname

    @property
    def IsSelect(self):
        return self.__isSelect
    @IsSelect.setter
    def IsSelect(self, isSelect):
        self.__isSelect = isSelect

    @property
    def IsVisible(self):
        return self.__isVisible
    @IsVisible.setter
    def IsVisible(self, isVisible):
        self.__isVisible = isVisible

    @property
    def WeaponId(self):
        return self.__weaponId
    @WeaponId.setter
    def WeaponId(self, weaponId):
        self.__weaponId = weaponId

    @property
    def SecondWeaponId(self):
        return self.__secondWeaponId
    @SecondWeaponId.setter
    def SecondWeaponId(self, weaponId):
        self.__secondWeaponId = weaponId

    def GetArmorId(self):
        return self.armorId

    def SetArmorId(self, armorId):
        self.armorId = armorId

    @property
    def Status(self):
        return self.__status
