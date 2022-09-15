# 横方向・縦方向のマスの数
# 動かせる部分は20*20だが、六角形表示のため上下左右に余分に作成している。
NUM_WIDTH = 22
NUM_HEIGHT = 22

# 色の設定
BOARD_COLOR = 'gray'        # 盤面全体（見えない位置）
VISIBLE_COLOR = 'white'     # ユニットから見える範囲（カラー）
DEAD_COLOR = 'red'          # 侵入不可エリア
OUT_LINE_COLOR = 'black'    # 枠線の色

# 中央座標の取り方
# (x,y)の時、(h_w*x, h_w1_4 + h_w3_4*y)

class Map:
    def __init__(self):
        '''コンストラクタ'''
        self.board = None       #   盤面上のユニットを管理する2次元リスト
        self.h_w = 45
        self.h_w1_4 = 45 / 4
        self.h_w1_2 = 45 / 2
        self.h_w3_4 = 45 * (3 / 4)

        # ゲームの初期化
        self.initMap()

    def initMap(self):
        '''マップの初期化を行う'''

        # 盤面上の石を管理する２次元リストを作成（最初は全てNone）
        #[[None for _ in range(10)] for _ in range(10)]
        self.board = [[None for j in range(NUM_WIDTH)] for i in range(NUM_HEIGHT)]

        self.m_xy = []
        # マスを描画    22 * 22 = 484
        for y in range(NUM_HEIGHT):
            for x in range(NUM_WIDTH):
                # 開始・終了座標を計算
                if y % 2 == 0:
                    #   北東の点
                    xne = self.h_w * (x + 1) - self.h_w1_2
                    yne = self.h_w1_4 + (self.h_w3_4 * y) - self.h_w1_4
                    #   北の点
                    xn = self.h_w1_2 + (self.h_w * x) - self.h_w1_2
                    yn = self.h_w3_4 * y - self.h_w1_4
                    #   北西の点
                    xns = self.h_w * x - self.h_w1_2   #0スタートなので、最初は0でいい
                    yns = yne
                    #   南西の点
                    xws = xns
                    yws = (self.h_w3_4 * (y + 1)) - self.h_w1_4
                    #   南の点
                    xw = xn
                    yw = self.h_w + (self.h_w3_4 * y) - self.h_w1_4
                    #   南東の点
                    xwe = xne
                    ywe = yws
                elif y % 2 == 1:
                    #   北東の点
                    xne = self.h_w * (x + 1) + self.h_w1_2 - self.h_w1_2
                    yne = self.h_w + (self.h_w3_4 * (y - 1)) - self.h_w1_4
                    #   北の点
                    xn = self.h_w * (x + 1) - self.h_w1_2
                    yn = self.h_w3_4 * y - self.h_w1_4
                    #   北西の点
                    xns = (self.h_w * x) + self.h_w1_2 - self.h_w1_2    #yが奇数なので、最初は22.5から
                    yns = yne
                    #   南西の点
                    xws = xns
                    yws = self.h_w3_4 * (y + 1) - self.h_w1_4
                    #   南の点
                    xw = xn
                    yw = self.h_w1_4 + (self.h_w3_4 * (y +1)) - self.h_w1_4
                    #   南東の点
                    xwe = xne
                    ywe = yws
                self.m_xy.append([x, y, xne, yne, xn, yn, xns, yns, xws, yws, xw, yw, xwe, ywe])
        return self.m_xy
