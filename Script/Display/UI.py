import tkinter as tk
import sys, os
# マップ表示のクラス
sys.path.append('../../Script/Data/')
from Script.Data.GameData import GameData

CANVAS_WIDTH =  179
CANVAS_HEIGHT = 960

# 色の設定
white = (255,255,255)
black = (0,0,0)
gray = (128, 128, 128)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

BOARD_COLOR = white       # 盤面全体（見えない位置）
OUT_LINE_COLOR = black    # 枠線の色
TEXT_COLOR = black        # 文字の色


class GameDraw:
    def __init__(self, master):
        '''コンストラクタ'''
        self.master = master    #   親ウィジェット
        self.createWidgets()

        # マップの描画
        self.drawMap(self.map)

    def createWidgets(self):
        '''ウィジェットを作成・配置する'''

        #   キャンバスの作成
        self.canvas = tk.Canvas(
            self.master,
            bg = BOARD_COLOR,
            width   = CANVAS_WIDTH,     # +1は枠線描画のため
            height  = CANVAS_HEIGHT, # +1は枠線描画のため
            highlightthickness = 0
        )
        self.canvas.pack(side = tk.RIGHT)


