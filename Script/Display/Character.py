import random

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

h_w = 45
h_w1_4 = 45 / 4
h_w1_2 = 45 / 2
h_w3_4 = 45 * (3 / 4)

class Character:
    def __init__(self, x_i, x_j, y_i, y_j):
        #self.p_w = 40
        # ユニットが同じ位置に生成されないように確認
        while True:
            xl = rand_ints_x(x_i, x_j)
            yl = rand_ints_y(y_i, y_j)
            z = rand_ints_check(xl, yl)
            if z == True:
                break

        self.prepareUnit(xl, yl)

        self.xl = xl
        self.yl = yl

    def prepareUnit(self, xl, yl):
        # (x,y)のマスの中心座標を計算
        self.xy = []
        for num in range(6):
            # 開始・終了座標を計算
            if yl[num] % 2 == 0:
                # 左上のx
                xns = h_w * xl[num] - h_w1_2 + 5
                # 左上のy
                yn = h_w3_4 * yl[num] - h_w1_4 + 5
                # 右下のx
                xne = h_w * (xl[num] + 1) - h_w1_2 - 5
                # 右下のy
                yw = h_w + (h_w3_4 * yl[num]) - h_w1_4 - 5 
            elif yl[num] % 2 == 1:
                # 左上のx
                xns = (h_w * xl[num]) + h_w1_2 - h_w1_2 + 5
                # 左上のy
                yn = h_w3_4 * yl[num] - h_w1_4 + 5
                # 右下のx
                xne = h_w * (xl[num] + 1) + h_w1_2 - h_w1_2 - 5
                # 右下のy
                yw = h_w1_4 + (h_w3_4 * (yl[num] +1)) - h_w1_4 - 5
            
            # (x, y)座標
            tagname = "(" + str(xl[num]) + "," + str(yl[num]) + ")"
            self.xy.append([num, xl[num], yl[num], xns, yn, xne, yw, tagname])

        return self.xy


class Player(Character):
    def __init__(self):
        super().__init__(6, 15, 16, 20)

#    def preparePlayer(self):
#        # (x,y)のマスの中心座標を計算
#        self.p_xy = []
#        for num in range(6):
#            # 開始・終了座標を計算
#            if self.p_yl[num] % 2 == 0:
#                # 左上のx
#                xns = self.h_w * self.p_xl[num] - self.h_w1_2 + 5
#                # 左上のy
#                yn = self.h_w3_4 * self.p_yl[num] - self.h_w1_4 + 5
#                # 右下のx
#                xne = self.h_w * (self.p_xl[num] + 1) - self.h_w1_2 - 5
#                # 右下のy
#                yw = self.h_w + (self.h_w3_4 * self.p_yl[num]) - self.h_w1_4 - 5 
#            elif self.p_yl[num] % 2 == 1:
#                # 左上のx
#                xns = (self.h_w * self.p_xl[num]) + self.h_w1_2 - self.h_w1_2 + 5
#                # 左上のy
#                yn = self.h_w3_4 * self.p_yl[num] - self.h_w1_4 + 5
#                # 右下のx
#                xne = self.h_w * (self.p_xl[num] + 1) + self.h_w1_2 - self.h_w1_2 - 5
#                # 右下のy
#                yw = self.h_w1_4 + (self.h_w3_4 * (self.p_yl[num] +1)) - self.h_w1_4 - 5
#            
#            # (x, y)座標
#            tagname = "(" + str(self.p_xl[num]) + "," + str(self.p_yl[num]) + ")"
#            self.p_xy.append([num, self.p_xl[num], self.p_yl[num], xns, yn, xne, yw, tagname])
#
#        return self.p_xy


class Enemy(Character):
    def __init__(self):
        super().__init__(6, 15, 1, 5)

#    def prepareEnemy(self):
#            # (x,y)のマスの中心座標を計算
#        self.e_xy = []
#        for num in range(6):
#            # 開始・終了座標を計算
#            if self.e_yl[num] % 2 == 0:
#                # 左上のx
#                xns = self.h_w * self.e_xl[num] - self.h_w1_2 + 5
#                # 左上のy
#                yn = self.h_w3_4 * self.e_yl[num] - self.h_w1_4 + 5
#                # 右下のx
#                xne = self.h_w * (self.e_xl[num] + 1) - self.h_w1_2 - 5
#                # 右下のy
#                yw = self.h_w + (self.h_w3_4 * self.e_yl[num]) - self.h_w1_4 - 5 
#            elif self.e_yl[num] % 2 == 1:
#                # 左上のx
#                xns = (self.h_w * self.e_xl[num]) + self.h_w1_2 - self.h_w1_2 + 5
#                # 左上のy
#                yn = self.h_w3_4 * self.e_yl[num] - self.h_w1_4 + 5
#                # 右下のx
#                xne = self.h_w * (self.e_xl[num] + 1) + self.h_w1_2 - self.h_w1_2 - 5
#                # 右下のy
#                yw = self.h_w1_4 + (self.h_w3_4 * (self.e_yl[num] +1)) - self.h_w1_4 - 5
#            
#            # (x, y)座標
#            tagname = "(" + str(self.e_xl[num]) + "," + str(self.e_yl[num]) + ")"
#            self.e_xy.append([num, self.e_xl[num], self.e_yl[num], xns, yn, xne, yw, tagname])
#
#        return self.e_xy

#    def updatePlayer(self, num):    #　行動力でforの回数が変更される予定
        # ほぼ同時に動かす想定なので、その辺を考えましょう
        # 移動先を配列で管理して描画する設定
#        for num in range(6):
            # 開始・終了座標を計算
#            if self.p_xy[num][2] % 2 == 0:
                # 左上のx
#                xns = self.h_w * self.p_xy[num][1] - self.h_w1_2 + 5
                # 左上のy
#                yn = self.h_w3_4 * self.p_xy[num][2] - self.h_w1_4 + 5
                # 右下のx
#                xne = self.h_w * (self.p_xy[num][1] + 1) - self.h_w1_2 - 5
                # 右下のy
#                yw = self.h_w + (self.h_w3_4 * self.p_xy[num][2]) - self.h_w1_4 - 5 
#            elif self.p_xy[num][2] % 2 == 1:
                # 左上のx
#                xns = (self.h_w * self.p_xy[num][1]) + self.h_w1_2 - self.h_w1_2 + 5
                # 左上のy
#                yn = self.h_w3_4 * self.p_xy[num][2] - self.h_w1_4 + 5
                # 右下のx
#                xne = self.h_w * (self.p_xy[num][1] + 1) + self.h_w1_2 - self.h_w1_2 - 5
                # 右下のy
#                yw = self.h_w1_4 + (self.h_w3_4 * (self.p_xy[num][2] +1)) - self.h_w1_4 - 5
            
            # (x, y)座標
#            tagname = "(" + str(self.p_xy[num][1]) + "," + str(self.p_xy[num][2]) + ")"
#            self.p_xy[num][1] = self.p_u_xy[num][1]
#            self.p_xy[num][2] = self.p_u_xy[num][2]
#            self.p_xy[num][3] = xns
#            self.p_xy[num][4] = yn
#            self.p_xy[num][5] = xne
#            self.p_xy[num][6] = xne
#            self.p_xy[num][7] = tagname
            #self.p_xy.append([num, self.p_xy[num][1], self.p_xy[num][2], , , xne, yw, tagname])

#        return self.p_xy



