import random
# 横方向・縦方向のマスの数
# 動かせる部分は20*20だが、六角形表示のため上下左右に余分に作成している。
NUM_WIDTH = 30
NUM_HEIGHT = 24
# 中央座標の取り方
# (x,y)の時、(h_w*x, h_w1_4 + h_w3_4*y)
# 原作にはないが建物破壊をするシステムを採用するのであれば、可変可能なマップを生成できるのが良い
# 何かしらアルゴリズムを組んで下の建物描画方法切り替えで対応する?

# 六角形の建物にする

class MapManager:
    def __init__(self):
        """マップ生成"""
        self.board = [ [0 for i in range(NUM_WIDTH)] for j in range(NUM_HEIGHT)]

        for y in range(NUM_HEIGHT):
            for x in range(NUM_WIDTH):
                if y == 0 or y == 1 or y >= 22:
                    self.board[y][x] = -1
                else:
                    if x == 0 or x == 1 or x >= 22:
                        self.board[y][x] = -1
                    else:
                        if (2 < y and y < 6) or (17 < y and y < 21) or (8 < x and x < 17):
                            """ユニットの生成位置"""
                            self.board[y][x] = 0
                        else:
                            # ここで5*5のランダムマップを代入する（後々）
                            self.board[y][x] = 0

mapmana = MapManager()


class Map:
    def __init__(self):
        '''コンストラクタ''' 
        # 1回で登れる高さは2まで
        # -1:進行不可, 0:平地, 1:高さ1の建物, 2:高さ2の建物, 3:高さ3の建物, 4:高さ4の建物, 5:高さ5の建物, 6: 高さ6の建物
        # 盤面上のマップを管理する2次元リスト
        self.board = [  [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 1, 3, 0, 3, 3, 1, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 3, 1, 0, 3, 3, 1, 1, 2, 2, 2, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        self.h_w = 50.15
        self.h_w1_4 = self.h_w / 4
        self.h_w1_2 = self.h_w / 2
        self.h_w3_4 = self.h_w * (3 / 4)

        self.h_h = 57.3
        self.h_h3_4 = self.h_h * (3 / 4)
        self.h_h1_4 = self.h_h / 4
        self.h_h1_2 = self.h_h / 2

        self.space = (0, 0)
        # ゲームの初期化
        self.initMap()


    def initMap(self):
        '''マップの初期化を行う'''

        # 盤面上の石を管理する２次元リストを作成（最初は全てNone）
        #[[None for _ in range(10)] for _ in range(10)]
        #self.board = [[None for j in range(NUM_WIDTH)] for i in range(NUM_HEIGHT)]

        self.m_xy = []
        # マスを描画    30 * 30 = 900
        for y in range(NUM_HEIGHT):
            for x in range(NUM_WIDTH):
                # 開始・終了座標を計算
                if y % 2 == 0:
                    #   北東の点
                    xne = self.h_w * (x + 1) - self.h_w1_2
                    yne = self.h_h1_4 + (self.h_h3_4 * y) - self.h_h3_4
                    #   北の点
                    xn = self.h_w1_2 + (self.h_w * x) - self.h_w1_2
                    yn = self.h_h3_4 * y - self.h_h3_4
                    #   北西の点
                    xnw = self.h_w * x - self.h_w1_2   #0スタートなので、最初は0でいい
                    ynw = yne
                    #   南西の点
                    xsw = xnw
                    ysw = (self.h_h3_4 * (y + 1)) - self.h_h3_4
                    #   南の点
                    xs = xn
                    ys = self.h_h + (self.h_h3_4 * y) - self.h_h3_4
                    #   南東の点
                    xse = xne
                    yse = ysw
                elif y % 2 == 1:
                    #   北東の点
                    xne = self.h_w * (x + 1) + self.h_w1_2 - self.h_w1_2
                    yne = self.h_h + (self.h_h3_4 * (y - 1)) - self.h_h3_4
                    #   北の点
                    xn = self.h_w * (x + 1) - self.h_w1_2
                    yn = self.h_h3_4 * y - self.h_h3_4
                    #   北西の点
                    xnw = (self.h_w * x) + self.h_w1_2 - self.h_w1_2    #yが奇数なので、最初は22.5から
                    ynw = yne
                    #   南西の点
                    xsw = xnw
                    ysw = self.h_h3_4 * (y + 1) - self.h_h3_4
                    #   南の点
                    xs = xn
                    ys = self.h_h1_4 + (self.h_h3_4 * (y + 1)) - self.h_h3_4
                    #   南東の点
                    xse = xne
                    yse = ysw
                board_number = self.board[y][x]

                self.m_xy.append([x, y, xne, yne, xn, yn, xnw, ynw, xsw, ysw, xs, ys, xse, yse, board_number])
        return self.m_xy

    def GetSpace(self):
        return self.space

    # 座標の設定
    def SetPos(self, x : int, y : int):
        self.space.x = x
        self.space.y = y
