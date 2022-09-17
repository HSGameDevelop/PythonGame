import pygame
from pygame.locals import *
import tkinter as tk
import sys, os
# マップ表示のクラス
#sys.path.append('../../Script/Display/')
#from Script.Display.Map import Map
import Map

# プレイヤー表示のクラス
#sys.path.append('../../Script/Display/')
#from Script.Display.Character import Character, Player, Enemy
import Character

CANVAS_WIDTH =  1101
CANVAS_HEIGHT = 960

# 色の設定
white = (255,255,255)
black = (0,0,0)
gray = (128, 128, 128)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

BOARD_COLOR = gray          # 盤面全体（見えない位置）
VISIBLE_COLOR = white       # ユニットから見える範囲（カラー）
DEAD_COLOR = red            # 侵入不可エリア
OUT_LINE_COLOR = black      # 枠線の色
YOUR_COLOR = blue           # あなたのユニットの色
ENEMY_COLOR = yellow        # 相手のユニットの色

class GameDraw:
    def __init__(self):
        '''コンストラクタ'''
        self.createWidgets()
        #self.map = Map()
        self.map = Map.Map()

        #self.characters = []
        #self.player = Player()
        #self.enemy = Enemy()
        #self.player = Character.Player()
        #self.enemy = Character.Enemy()

        # マップの描画
        self.drawMap(self.map)
        # プレイヤーの描画
        #self.createPlayer(self.player)
        # エネミーの描画
        #self.createEnemy(self.enemy)

    def createWidgets(self):
        '''ウィジェットを作成・配置する'''
        self.canvas = pygame.display.set_mode((1280, 960))

    def drawMap(self, map):
        # ６点指定 六角形
        for num in range(900):
            #pygame.draw.polygon(surface, (255,255,255), [(450, 60), (425, 17), (375, 17), (350, 60), (375, 103), (425, 103)], 0)
            #canvas.create_polygon( (450, 60), (425, 17), (375, 17), (350, 60), (375, 103), (425, 103))
            if map.m_xy[num][1] == 0 or map.m_xy[num][1] == 21 or map.m_xy[num][0] == 0 or map.m_xy[num][0] == 21:
                pygame.draw.polygon( self.canvas, DEAD_COLOR, [(map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][4], map.m_xy[num][5]), (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][8], map.m_xy[num][9]), (map.m_xy[num][10], map.m_xy[num][11]), (map.m_xy[num][12], map.m_xy[num][13])], 1)  #fill=DEAD_COLOR, outline=OUT_LINE_COLOR)
            else:
                pygame.draw.polygon( self.canvas, BOARD_COLOR, [(map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][4], map.m_xy[num][5]), (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][8], map.m_xy[num][9]), (map.m_xy[num][10], map.m_xy[num][11]), (map.m_xy[num][12], map.m_xy[num][13])], 1) #fill=BOARD_COLOR, outline=OUT_LINE_COLOR)

#    def createPlayer(self, player):
#        for num in range(6):
#            #[num, self.xl[num], self.yl[num], xns, yn, xne, yw, tagname]
#            self.canvas.create_oval(player.xy[num][3], player.xy[num][4], player.xy[num][5], player.xy[num][6], fill=YOUR_COLOR)
#            tag_length = len(player.xy[num][7])
#            if tag_length == 6:
#                self.canvas.create_text( player.xy[num][3] + 4, player.xy[num][4] + 10, text=player.xy[num][7], anchor=tk.NW)
#            elif tag_length == 7:
#                self.canvas.create_text( player.xy[num][3] + 2, player.xy[num][4] + 10, text=player.xy[num][7], anchor=tk.NW)
#
#
#    def createEnemy(self, player):
#        for num in range(6):
#            #[num, self.xl[num], self.yl[num], xns, yn, xne, yw, tagname]
#            self.canvas.create_oval(player.xy[num][3], player.xy[num][4], player.xy[num][5], player.xy[num][6], fill=ENEMY_COLOR)
#            tag_length = len(player.xy[num][7])
#            if tag_length == 5:
#                self.canvas.create_text( player.xy[num][3] + 6, player.xy[num][4] + 10, text=player.xy[num][7], anchor=tk.NW)
#            elif tag_length == 6:
#                self.canvas.create_text( player.xy[num][3] + 4, player.xy[num][4] + 10, text=player.xy[num][7], anchor=tk.NW)

#    def updateDraw(self, player_infos):
        

    #def updateEnemy(self, player_infos):
    #    for x, y in player_infos:
    #        self.canvas.create_oval(
    #            xs, ys,
    #            xe, ye,
    #            fill=YOUR_COLOR
    #        )

pygame.init()
#app = tk.Tk()
#app.geometry("1280x960")
game = GameDraw()
#app.mainloop()

# ゲームループ
while True:
    #game.canvas.fill(black) # 背景を黒で塗りつぶす

    #game.Update()
    #game.Draw()
    
    # 画面を更新
    pygame.display.update()
    # 終了イベントを確認 --- (*5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

