
# 六角形のグリッドを描画する  from PIL import ImageFont, ImageDraw
import tkinter as tk

# キャンバスの横方向・縦方向のサイズ（px）
# 下の数値より大きいと六角形の表示が中途半端な状態のところが表示されてしまう。
CANVAS_WIDTH =  969
CANVAS_HEIGHT = 732

# 横方向・縦方向のマスの数
# 動かせる部分は20*20だが、六角形表示のため上下左右に余分に作成している。
NUM_WIDTH = 22
NUM_HEIGHT = 22

# 色の設定
BOARD_COLOR = 'gray'        # 盤面全体（見えない位置）
VISIBLE_COLOR = 'white'     # ユニットから見える範囲（カラー）
DEAD_COLOR = 'red'          # 侵入不可エリア
OUT_LINE_COLOR = 'black'    # 枠線の色


#六角形の幅 w = sqrt(3) * sizeと高さはh = 2 * sizeです。sqrt(3) は sin(60°) 　b/c   c=斜線
#(x, y)900*800 とすると　w = 45
# 中央座標の取り方
# (x,y)の時、(h_w*x, h_w1_4 + h_w3_4*y)

class Hexagon:
    def __init__(self, master):
        '''コンストラクタ'''

        self.master = master    #   親ウィジェット
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
        # マスを描画    22* 22 = 484
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
                #---６点指定 六角形
                #canvas.create_polygon( (450, 60), (425, 17), (375, 17), (350, 60), (375, 103), (425, 103))
                #if y == 0 or y == (NUM_HEIGHT - 1) or x == 0 or x == (NUM_WIDTH - 1):
                    #self.canvas.create_polygon(xne, yne, xn, yn, xns, yns, xws, yws, xw, yw, xwe, ywe, fill=DEAD_COLOR, outline=OUT_LINE_COLOR)
                #else:
                    #self.canvas.create_polygon(xne, yne, xn, yn, xns, yns, xws, yws, xw, yw, xwe, ywe, fill=BOARD_COLOR, outline=OUT_LINE_COLOR)
        


#app = tk.Tk()
#app.geometry("1280x960")
#app.title('player test')
#Hex = Hexagon(app)
#app.mainloop()
