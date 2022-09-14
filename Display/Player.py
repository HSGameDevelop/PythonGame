import tkinter as tk
import random

# 重複なし
def rand_ints_x():
    xl = []
    while len(xl) < 6:
        x = random.randint(6, 15)
        xl.append(x)
    return xl


def rand_ints_y():
    yl = []
    while len(yl) < 6:
        y = random.randint(16, 20)
        yl.append(y)
    return yl


def rand_ints_check(xl,yl):
    for x in range(5):
        for y in range(5):
            if xl[x] == xl[y] and x != y:
                if yl[x] == yl[y] and x != y:
                    return False
    return True


class Player:

    def __init__(self, master):
        self.master = master
        #self.base_y = VIEW_HEIGHT - self.right_image.height()

        self.p_w = 40

        # ユニットが同じ位置に生成されないように確認
        while True:
            xl = rand_ints_x()
            yl = rand_ints_y()
            z = rand_ints_check(xl, yl)
            if z == True:
                break
        print(xl)
        print(yl)

        # 六角形座標(x., y)の(xl[i], yl[i])のリスト
        self.xl = xl
        self.yl = yl
        
        self.h_w = 45
        self.h_w1_4 = 45 / 4
        self.h_w1_2 = 45 / 2
        self.h_w3_4 = 45 * (3 / 4)

        self.preparePlayer()

    def preparePlayer(self):        #ここはいらないけど計算を受け渡せるようにしたいので、後々移動
        # (x,y)のマスの中心座標を計算
        self.p_xy = []
        for num in range(6):
            # 開始・終了座標を計算
            if self.yl[num] % 2 == 0:
                # 左上のx
                xns = self.h_w * self.xl[num] - self.h_w1_2 + 5
                # 左上のy
                yn = self.h_w3_4 * self.yl[num] - self.h_w1_4 + 5
                # 右下のx
                xne = self.h_w * (self.xl[num] + 1) - self.h_w1_2 - 5
                # 右下のy
                yw = self.h_w + (self.h_w3_4 * self.yl[num]) - self.h_w1_4 - 5 
            elif self.yl[num] % 2 == 1:
                # 左上のx
                xns = (self.h_w * self.xl[num]) + self.h_w1_2 - self.h_w1_2 + 5
                # 左上のy
                yn = self.h_w3_4 * self.yl[num] - self.h_w1_4 + 5
                # 右下のx
                xne = self.h_w * (self.xl[num] + 1) + self.h_w1_2 - self.h_w1_2 - 5
                # 右下のy
                yw = self.h_w1_4 + (self.h_w3_4 * (self.yl[num] +1)) - self.h_w1_4 - 5
            
            # (x, y)座標
            tagname = "(" + str(self.xl[num]) + "," + str(self.yl[num]) + ")"
            self.p_xy.append([num, xns, yn, xne, yw, tagname])

        return self.p_xy
            #self.canvas.create_oval(xns, yn, xne, yw, fill=YOUR_COLOR)
            #tag_length = len(tagname)
            #if tag_length == 6:
            #    self.create_text( xns + 4, yn + 10, text=tagname, anchor=tk.NW)
            #elif tag_length == 7:
            #    self.create_text( xns + 2, yn + 10, text=tagname, anchor=tk.NW)



