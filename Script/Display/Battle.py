from re import S
import pygame
from pygame.locals import *
import sys, os
# マップ表示のクラス
from .Map import Map
#import Map

# プレイヤー表示のクラス
from .Character import Character, Player, Enemy
#import Character
sys.path.append('../../System/Game/')
from Script.System.Game.PgLib import PgLib
from Script.System.Game.GameSequenceBase import GameSequenceBase

CANVAS_WIDTH =  1280
CANVAS_HEIGHT = 960

# 色の設定
white = (255,255,255)
black = (0,0,0)
gray = (128, 128, 128)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
purple = (0, 255, 255)

BOARD_COLOR = gray          # 盤面全体（見えない位置）
VISIBLE_COLOR = white       # ユニットから見える範囲（カラー）
DEAD_COLOR = black          # 侵入不可エリア
DEAD_OUT_LINE_COLOR = black# 侵入不可エリア枠線
OUT_LINE_COLOR = black      # 枠線の色
YOUR_COLOR = blue           # あなたのユニットの色
ENEMY_COLOR = yellow        # 相手のユニットの色

class Battle(GameSequenceBase):
    def __init__(self, pgLib : PgLib) -> None:
        '''コンストラクタ'''
        self.pgLib = pgLib
        #self.createWidgets()
        self.map = Map()
        #self.map = Map.Map()
        

        #self.characters = []
        self.player = Player()
        self.enemy = Enemy()
        #self.player = Character.Player()
        #self.enemy = Character.Enemy()


    def Update(self):
        pass

    def Draw(self):
        self.screen = self.pgLib.GetScreen()
        # マップの描画
        self.drawMap(self.map)
        # プレイヤーの描画
        self.createPlayer(self.player)
        # エネミーの描画
        self.createEnemy(self.enemy)


#    def createWidgets(self):
#        '''ウィジェットを作成　main以降する時削除'''
#        screen = pygame.display.set_mode((1280, 960))

    def drawMap(self, map):
        # ６点指定 六角形
        for num in range(660):
            #pygame.draw.polygon(surface, (255,255,255), [(450, 60), (425, 17), (375, 17), (350, 60), (375, 103), (425, 103)], 0)
            #canvas.create_polygon( (450, 60), (425, 17), (375, 17), (350, 60), (375, 103), (425, 103))
            # y = map.m_xy[num][1]   x = map.m_xy[num][0]
            if map.m_xy[num][1] == 0 or map.m_xy[num][1] == 21 or map.m_xy[num][0] == 0 or map.m_xy[num][0] == 1 or map.m_xy[num][0] == 2 or map.m_xy[num][0] == 23 or map.m_xy[num][0] == 24 or map.m_xy[num][0] == 25:
                # 内側描画
                pygame.draw.polygon( self.screen, DEAD_COLOR, [(map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][4], map.m_xy[num][5]), (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][8], map.m_xy[num][9]), (map.m_xy[num][10], map.m_xy[num][11]), (map.m_xy[num][12], map.m_xy[num][13])])  #fill=DEAD_COLOR, outline=OUT_LINE_COLOR)
                # 枠線描画
                pygame.draw.polygon( self.screen, DEAD_OUT_LINE_COLOR, [(map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][4], map.m_xy[num][5]), (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][8], map.m_xy[num][9]), (map.m_xy[num][10], map.m_xy[num][11]), (map.m_xy[num][12], map.m_xy[num][13])], 1)
            else:
                # 内側描画
                pygame.draw.polygon( self.screen, BOARD_COLOR, [(map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][4], map.m_xy[num][5]), (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][8], map.m_xy[num][9]), (map.m_xy[num][10], map.m_xy[num][11]), (map.m_xy[num][12], map.m_xy[num][13])]) #fill=BOARD_COLOR, outline=OUT_LINE_COLOR)
                # 枠線描画
                pygame.draw.polygon( self.screen, OUT_LINE_COLOR, [(map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][4], map.m_xy[num][5]), (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][8], map.m_xy[num][9]), (map.m_xy[num][10], map.m_xy[num][11]), (map.m_xy[num][12], map.m_xy[num][13])], 1)

    def createPlayer(self, player):
        for num in range(6):
            font = pygame.font.Font(None, 15)
            #[num, self.xl[num], self.yl[num], xc, yc, tagname]
            pygame.draw.circle(self.screen, blue, (player.xy[num][3], player.xy[num][4]), 21)
            #self.screen.create_oval(player.xy[num][3], player.xy[num][4], player.xy[num][5], player.xy[num][6], fill=YOUR_COLOR)
            tag_length = len(player.xy[num][5])
            if tag_length == 6:
                text = font.render(player.xy[num][5], True, (255,255,255))
                self.screen.blit(text, [player.xy[num][3] - 12, player.xy[num][4]])
                #self.screen.create_text( player.xy[num][3] + 4, player.xy[num][4] + 10, text=player.xy[num][7], anchor=tk.NW)
            elif tag_length == 7:
                text = font.render(player.xy[num][5], True, (255,255,255))
                self.screen.blit(text, [player.xy[num][3] - 15, player.xy[num][4]])
                #self.screen.create_text( player.xy[num][3] + 2, player.xy[num][4] + 10, text=player.xy[num][7], anchor=tk.NW)


    def createEnemy(self, enemy):
        for num in range(6):
            font = pygame.font.Font(None, 15)
            #[num, self.xl[num], self.yl[num], xc, yc, tagname]
            pygame.draw.circle(self.screen, yellow, (enemy.xy[num][3], enemy.xy[num][4]), 21)
            #self.screen.create_oval(enemy.xy[num][3], enemy.xy[num][4], enemy.xy[num][5], enemy.xy[num][6], fill=ENEMY_COLOR)
            tag_length = len(enemy.xy[num][5])
            if tag_length == 5:
                text = font.render(enemy.xy[num][5], True, (255,0,0))
                self.screen.blit(text, [enemy.xy[num][3] - 12, enemy.xy[num][4]])
                #self.screen.create_text( enemy.xy[num][3] + 6, enemy.xy[num][4] + 10, text=enemy.xy[num][7], anchor=tk.NW)
            elif tag_length == 6:
                text = font.render(enemy.xy[num][5], True, (255,0,0))
                self.screen.blit(text, [enemy.xy[num][3] - 10, enemy.xy[num][4]])
                #self.screen.create_text( enemy.xy[num][3] + 4, enemy.xy[num][4] + 10, text=enemy.xy[num][7], anchor=tk.NW)

    def updatePlayer(self, player):
        for num in range(6):
            font = pygame.font.Font(None, 15)
            #[num, self.xl[num], self.yl[num], xc, yc, tagname]
            pygame.draw.circle(self.screen, blue, (player.xy[num][3], player.xy[num][4]), 21)
            #self.screen.create_oval(player.xy[num][3], player.xy[num][4], player.xy[num][5], player.xy[num][6], fill=YOUR_COLOR)
            tag_length = len(player.xy[num][5])
            if tag_length == 6:
                text = font.render(player.xy[num][5], True, (255,255,255))
                self.screen.blit(text, [player.xy[num][3] - 12, player.xy[num][4]])
                #self.screen.create_text( player.xy[num][3] + 4, player.xy[num][4] + 10, text=player.xy[num][7], anchor=tk.NW)
            elif tag_length == 7:
                text = font.render(player.xy[num][5], True, (255,255,255))
                self.screen.blit(text, [player.xy[num][3] - 15, player.xy[num][4]])
                #self.screen.create_text( player.xy[num][3] + 2, player.xy[num][4] + 10, text=player.xy[num][7], anchor=tk.NW)

    def updateEnemy(self, enemy):
            for num in range(6):
                font = pygame.font.Font(None, 15)
                #[num, self.xl[num], self.yl[num], xc, yc, tagname]
                pygame.draw.circle(self.screen, yellow, (enemy.xy[num][3], enemy.xy[num][4]), 21)
                #self.screen.create_oval(enemy.xy[num][3], enemy.xy[num][4], enemy.xy[num][5], enemy.xy[num][6], fill=ENEMY_COLOR)
                tag_length = len(enemy.xy[num][5])
                if tag_length == 5:
                    text = font.render(enemy.xy[num][5], True, (255,0,0))
                    self.screen.blit(text, [enemy.xy[num][3] - 12, enemy.xy[num][4]])
                    #self.screen.create_text( enemy.xy[num][3] + 6, enemy.xy[num][4] + 10, text=enemy.xy[num][7], anchor=tk.NW)
                elif tag_length == 6:
                    text = font.render(enemy.xy[num][5], True, (255,0,0))
                    self.screen.blit(text, [enemy.xy[num][3] - 10, enemy.xy[num][4]])
                    #self.screen.create_text( enemy.xy[num][3] + 4, enemy.xy[num][4] + 10, text=enemy.xy[num][7], anchor=tk.NW)

    def Turn(self):
        pass

    def Timer(self):
        pass

#    def updateDraw(self, player):
#        for num in range(6):
#            font = pygame.font.Font(None, 15)
#            #[num, self.xl[num], self.yl[num], xc, yc, tagname]
#            pygame.draw.circle(screen, blue, (player.xy[num][3] * 1.5, player.xy[num][4] * 1.5), 21)
#            #screen.create_oval(player.xy[num][3], player.xy[num][4], player.xy[num][5], player.xy[num][6], fill=YOUR_COLOR)
#            tag_length = len(player.xy[num][5])
#            if tag_length == 6:
#                text = font.render(player.xy[num][5], True, (255,255,255))
#                screen.blit(text, [player.xy[num][3] * 1.5 - 12, player.xy[num][4] * 1.5])
#                #screen.create_text( player.xy[num][3] + 4, player.xy[num][4] + 10, text=player.xy[num][7], anchor=tk.NW)
#            elif tag_length == 7:
#                text = font.render(player.xy[num][5], True, (255,255,255))
#                screen.blit(text, [player.xy[num][3] * 1.5 - 15, player.xy[num][4] * 1.5])
                #screen.create_text( player.xy[num][3] + 2, player.xy[num][4] + 10, text=player.xy[num][7], anchor=tk.NW)

    #def updateEnemy(self, player_infos):
    #    for x, y in player_infos:
    #        screen.create_oval(
    #            xs, ys,
    #            xe, ye,
    #            fill=YOUR_COLOR
    #        )

#pygame.init()
#game = BattleDraw()
#
## ゲームループ
#while True:
#    #game.canvas.fill(black) # 背景を黒で塗りつぶす
#
#    #game.Update()
#    #game.Draw()
#    
#    # 画面を更新
#    pygame.display.update()
#    game.updateDraw(game.enemy)
#    pygame.display.update()
#    # 終了イベントを確認 --- (*5)
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()

