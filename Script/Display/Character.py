import random
import sys, os

sys.path.append('../System/Util/')
from ..System.Util.GameObject import GameObject
sys.path.append('../System/Data/')
from ..Data.GameData import GameData

#sys.path.append('../../System/Util/')
#from ..System.Util.GameObject import GameObject

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
        self.gd = GameData()
        self.gd.LoadData()
        self.unit_side = side

        self.id, self.xl, self.yl, self.x, self.y, self.tagname = self.prepareUnit(xl, yl, self.gd.GetCharacterDataFromId(num).characterId )
        self.characterName  = self.gd.GetCharacterDataFromId(num).characterName         # キャラクター名
        self.weaponId       = self.gd.GetCharacterDataFromId(num).weaponId              # 武器ID
        self.actionPower    = self.gd.GetCharacterDataFromId(num).actionPower           # 行動力
        self.skillSetId     = self.gd.GetCharacterDataFromId(num).skillSetId            # スキルセットID

        self.weaponName     = self.gd.GetWeaponDataFromId(self.weaponId).weaponName     # 武器名
        self.range          = self.gd.GetWeaponDataFromId(self.weaponId).range          # 射程距離
        self.power          = self.gd.GetWeaponDataFromId(self.weaponId).power          # 攻撃力
        self.consumption    = self.gd.GetWeaponDataFromId(self.weaponId).consumption    # 攻撃時の行動力消費
        self.angle          = self.gd.GetWeaponDataFromId(self.weaponId).angle          # 角度
        self.powerFlag      = self.gd.GetWeaponDataFromId(self.weaponId).powerFlag      # ユニットの攻撃力分を加算するかどうか
        self.plusdown       = self.gd.GetWeaponDataFromId(self.weaponId).plusdown       # 武器装備時の行動力の増減


    def prepareUnit(self, xl, yl, id):
        # (x,y)のマスの中心座標を計算
        #self.xy = []
        if yl % 2 == 0:
            x = h_w * xl
            y = h_h3_4 * yl - h_h1_4
            self.SetPos(x, y)
        elif yl % 2 == 1:
            x = h_w1_2 + (xl * h_w)
            y = (h_h3_4 * yl) - h_h1_4
            self.SetPos(x, y)
        
        # (x, y)座標
        tagname = "(" + str(xl) + "," + str(yl) + ")"
        #self.xy.append([id, xl, yl, x, y, tagname])
        return id, xl, yl, x, y, tagname


class Player(Character):
    def __init__(self, xl, yl, num):
        super().__init__(xl, yl, PLAYER, num)


class Enemy(Character):
    def __init__(self, xl, yl, num, p_num):
        super().__init__(xl, yl, ENEMY, num + p_num)

