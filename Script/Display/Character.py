import random
import sys, os

sys.path.append('../System/Util/')
from ..System.Util.GameObject import GameObject
sys.path.append('../System/Data/')
from ..Data.GameData import GameData

#sys.path.append('../../System/Util/')
#from ..System.Util.GameObject import GameObject

# キャラの視界を設定マップへ反映するように追加

#  player 重複なし
def rand_ints_x(i, j):
    xl = []
    while len(xl) < 6:
        x = random.randint(i, j)
        xl.append(x)
    return xl

def rand_ints_y(i, j):
    yl = []
    while len(yl) < 6:
        y = random.randint(i, j)
        yl.append(y)
    return yl

def rand_ints_check(xl,yl):
    for x in range(6):
        for y in range(6):
            if xl[x] == xl[y] and x != y:
                if yl[x] == yl[y] and x != y:
                    return False
    return True

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
move_speed = 10

class Character(GameObject):
    def __init__(self, x_i, x_j, y_i, y_j, side):
        super().__init__()

        #self.p_w = 40
        # ユニットが同じ位置に生成されないように確認
        while True:
            xl = rand_ints_x(x_i, x_j)
            yl = rand_ints_y(y_i, y_j)
            z = rand_ints_check(xl, yl)
            if z == True:
                break

        self.gd = GameData()
        self.gd.LoadData()
        self.unit_side = side

        self.prepareUnit(xl, yl, self.unit_side, self.gd.GetCharacterDataFromId(1).characterId )
        #self.unit = GameObject(size=(20, 20) , image=None, moveSpeed=move_speed, position=(self.xc, self.yc))
        #print(self.gd.GetCharacterDataFromId(1).characterName)


    def prepareUnit(self, xl, yl, unit, id):
        # (x,y)のマスの中心座標を計算
        self.xy = []
        for num in range(6):
            # 開始・終了座標を計算
            if yl[num] % 2 == 0:
                x = h_w * xl[num]
                y = h_h3_4 * yl[num] - h_h1_4
                self.SetPos(x, y)
            elif yl[num] % 2 == 1:
                x = h_w1_2 + (xl[num] * h_w)
                y = (h_h3_4 * yl[num]) - h_h1_4
                self.SetPos(x, y)
            
            # (x, y)座標
            tagname = "(" + str(xl[num]) + "," + str(yl[num]) + ")"
            self.xy.append([id, xl[num], yl[num], x, y, tagname])

        return self.xy


class Player(Character):
    def __init__(self):
        super().__init__(8, 17, 17, 21, PLAYER)


class Enemy(Character):
    def __init__(self):
        super().__init__(8, 17, 2, 6, ENEMY)

