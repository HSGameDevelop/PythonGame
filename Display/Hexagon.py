
# 六角形のグリッドを描画する  from PIL import ImageFont, ImageDraw
import math
import tkinter as tk

# キャンバスの横方向・縦方向のサイズ（px）
CANVAS_WIDTH =  968
CANVAS_HEIGHT = 731


# 横方向・縦方向のマスの数
NUM_WIDTH = 22
NUM_HEIGHT = 22

# 色の設定
BOARD_COLOR = 'gray' # 盤面全体（見えない位置）
VISIBLE_COLOR = 'white' # ユニットから見える範囲（カラー）

#六角形の幅 w = sqrt(3) * sizeと高さはh = 2 * sizeです。sqrt(3) は sin(60°) 　b/c   c=斜線
#(x, y)900*800 とすると　w = 45
h_w = 45
h_w1_4 = 45 / 4
h_w1_2 = 45 / 2
h_w3_4 = 45 * (3 / 4)
# 座標(0,1)は (w1_2)が一番低いx座標 

# hexgridの縦横サイズ
#print(PX)
#PY = PX * math.sqrt(3)/2
#print(PY)

# 一辺の長さ
#L = PX / math.sqrt(3)
#print(L)

class Hexagon:
    def __init__(self, master):
        '''コンストラクタ'''

        self.master = master    #   親ウィジェット

        # ウィジェットの作成
        self.createWidgets()

        # ゲームの初期化
        self.initMove()


    def createWidgets(self):
        '''ウィジェットを作成・配置する'''
    
        #   キャンバスの作成
        self.canvas = tk.Canvas(
            self.master,
            bg = BOARD_COLOR,
            width=   CANVAS_WIDTH + 1,     # +1は枠線描画のため
            height = CANVAS_HEIGHT + 1, # +1は枠線描画のため
            highlightthickness = 0
        )
        self.canvas.pack(padx = 120, pady = 50)


    def initMove(self):
        '''ゲームの初期化を行う'''

        # 盤面上の石を管理する２次元リストを作成（最初は全てNone）
        #[[None for _ in range(10)] for _ in range(10)]
        #self.board = [[None] * (NUM_WIDTH) for i in range(NUM_HEIGHT)]

        # マスを描画
        for y in range(NUM_HEIGHT):
            for x in range(NUM_WIDTH):
                # 開始・終了座標を計算
                if y % 2 == 0:
                    #   北東の点
                    xne = h_w * (x + 1) - h_w1_2
                    yne = h_w1_4 + (h_w3_4 * y) - h_w1_4
                    #   北の点
                    xn = h_w1_2 + (h_w * x) - h_w1_2
                    yn = h_w3_4 * y - h_w1_4
                    #   北西の点
                    xns = h_w * x - h_w1_2   #0スタートなので、最初は0でいい
                    yns = yne
                    #   南西の点
                    xws = xns
                    yws = (h_w3_4 * (y + 1)) - h_w1_4
                    #   南の点
                    xw = xn
                    yw = h_w + (h_w3_4 * y) - h_w1_4
                    #   南東の点
                    xwe = xne
                    ywe = yws
                elif y % 2 == 1:
                    #   北東の点
                    xne = h_w * (x + 1) + h_w1_2 - h_w1_2
                    yne = h_w + (h_w3_4 * (y - 1)) - h_w1_4
                    #   北の点
                    xn = h_w * (x + 1) - h_w1_2
                    yn = h_w3_4 * y - h_w1_4
                    #   北西の点
                    xns = (h_w * x) + h_w1_2 - h_w1_2    #yが奇数なので、最初は22.5から
                    yns = yne
                    #   南西の点
                    xws = xns
                    yws = h_w3_4 * (y + 1) - h_w1_4
                    #   南の点
                    xw = xn
                    yw = h_w1_4 + (h_w3_4 * (y +1)) - h_w1_4
                    #   南東の点
                    xwe = xne
                    ywe = yws

                #---６点指定 六角形
                #canvas.create_polygon( (450, 60), (425, 17), (375, 17), (350, 60), (375, 103), (425, 103))
                if y == 0 or y == (NUM_HEIGHT - 1) or x == 0 or x == (NUM_WIDTH - 1):
                    self.canvas.create_polygon(xne, yne, xn, yn, xns, yns, xws, yws, xw, yw, xwe, ywe, fill='red', outline='white')
                else:
                    self.canvas.create_polygon(xne, yne, xn, yn, xns, yns, xws, yws, xw, yw, xwe, ywe, fill='black', outline='white')

                if y % 2 == 0 and x == (NUM_WIDTH - 1):
                    #   北東の点
                    xne = h_w * (x + 1) - h_w1_2
                    yne = h_w1_4 + (h_w3_4 * y) - h_w1_4
                    #   北の点
                    xn = h_w1_2 + (h_w * x) - h_w1_2
                    yn = h_w3_4 * y - h_w1_4
                    #   北西の点
                    xns = h_w * x - h_w1_2   #0スタートなので、最初は0でいい
                    yns = yne
                    #   南西の点
                    xws = xns
                    yws = (h_w3_4 * (y + 1)) - h_w1_4
                    #   南の点
                    xw = xn
                    yw = h_w + (h_w3_4 * y) - h_w1_4
                    #   南東の点
                    xwe = xne
                    ywe = yws
                    self.canvas.create_polygon(xne, yne, xn, yn, xns, yns, xws, yws, xw, yw, xwe, ywe, fill='red', outline='white')


# スクリプト処理ここから
app = tk.Tk()
app.geometry("1280x960")
app.title('move')
move = Hexagon(app)
app.mainloop()

