import random
import sys, os

from ...Util.GameObject import GameObject
from ..Data.GameData import GameData
from ..Data.ColorList import ColorList

# キャラの視界を設定マップへ反映するように追加

h_w = 50.15
h_w1_4 = h_w / 4
h_w1_2 = h_w / 2
h_w3_4 = h_w * (3 / 4)

h_h = 57.3
h_h3_4 = h_h * (3 / 4)
h_h1_4 = h_h / 4
h_h1_2 = h_h / 2

PLAYER = 0
ENEMY = 1


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
        self.isSelect = False
        self.isVisible = False

        self.xl, self.yl, self.x, self.y, self.tagname = self.prepareUnit(xl, yl)
        self.ID = num
        if self.unit_side == 0:
            self.chara = random.randint(1, 25)  # excelのプレイヤーの種類
        else:
            self.chara = random.randint(26, 50) # excelのエネミーの種類
        
        self.characterid = GameData.GetCharacterDataFromId(self.chara).characterId                        # キャラクターID
        self.characterName  = GameData.GetCharacterDataFromId(self.chara).characterName          # キャラクター名
        self.ActionPower      = GameData.GetCharacterDataFromId(self.chara).actionpower          # 行動力
        self.HitPoint    = GameData.GetCharacterDataFromId(self.chara).hitpoint                  # HP
        self.AttackPoint    = GameData.GetCharacterDataFromId(self.chara).attackpoint            # 攻撃力
        self.DeffencePoint     = GameData.GetCharacterDataFromId(self.chara).defensepoint        # 防御力
        self.AvoidancePoint       = GameData.GetCharacterDataFromId(self.chara).avoidancepoint   # 回避力
        self.TechnologyPoint    = GameData.GetCharacterDataFromId(self.chara).technologypoint    # 技術力
        self.Visible    = GameData.GetCharacterDataFromId(self.chara).visible                    # 視界

        self.weaponId1 = None
        self.weaponId2 = None
        self.armorId = None

        #self.weaponName     = GameData.GetWeaponDataFromId().weaponName     # 武器名
        #self.range          = GameData.GetWeaponDataFromId().range          # 射程距離
        #self.power          = GameData.GetWeaponDataFromId().power          # 攻撃力
        #self.actioncost    = GameData.GetWeaponDataFromId().actioncost    # 攻撃時の行動力消費
        #self.angle          = GameData.GetWeaponDataFromId().angle          # 角度
        #self.powerFlag      = GameData.GetWeaponDataFromId().powerFlag      # ユニットの攻撃力分を加算するかどうか
        #self.plusdown       = GameData.GetWeaponDataFromId().plusdown       # 武器装備時の行動力の増減
        self.SetSelect(self.isSelect)
        self.SetVisible(self.isVisible)


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

    def GetSelect(self):
        return self.isSelect

    def SetSelect(self, select):
        self.isSelect = select

    def GetVisible(self):
        return self.isVisible

    def SetVisible(self, visible):
        self.isVisible = visible

    def GetWeaponId1(self):
        return self.weaponId1

    def SetWeaponId1(self, weaponId):
        self.weaponId1 = weaponId

    def GetWeaponId2(self):
        return self.weaponId2

    def SetWeaponId2(self, weaponId):
        self.weaponId2 = weaponId

    def GetArmorId(self):
        return self.armorId

    def SetArmorId(self, armorId):
        self.armorId = armorId

class Player(Character):
    def __init__(self, xl, yl, num):
        super().__init__(xl, yl, PLAYER, num)

    def PlayerDraw(self):
        if self.isVisible == True:
            if self.isSelect == True:
                self.Draw(ColorList.LIGHTBLUE)
            else:
                self.Draw(ColorList.BLUE)
        else:
            if self.isSelect == True:
                self.Draw(ColorList.BLUE)
            else:
                self.Draw(ColorList.DARKBLUE)


class Enemy(Character):
    def __init__(self, xl, yl, num, p_num):
        super().__init__(xl, yl, ENEMY, num + p_num)

    def EnemyDraw(self):
        if self.isVisible == True:
            if self.isSelect == True:
                self.Draw(ColorList.LIGHTYELLOW)
            else:
                self.Draw(ColorList.YELLOW)
        else:
            if self.isSelect == True:
                self.Draw(ColorList.YELLOW)
            else:
                self.Draw(ColorList.OLIVE)
