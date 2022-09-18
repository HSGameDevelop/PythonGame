from enum import Enum
import time
import pygame
from pygame.locals import *
from math import pi
import math
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

# 円タイマーの中央座標
TIMER_X = 1230
TIMER_Y = 50

MAX_COUNTER = 30
CIRCLE_WIDTH_OUT = 40
CIRCLE_WIDTH_IN = 35

TURN_DISPLAY = 150

FPS = 60

# 色の設定
white = (255,255,255)
black = (0,0,0)
gray = (128, 128, 128)
blue = (0, 0, 255)
red_down = (122, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
purple = (255, 0, 255)
green = (0, 255, 0)
orange = (200, 100, 0)
pale_green = (0, 255, 100)
pale_black = (50, 50, 50)

BOARD_COLOR = gray          # 盤面全体（見えない位置）
VISIBLE_COLOR = white       # ユニットから見える範囲（カラー）
DEAD_COLOR = red_down          # 侵入不可エリア
DEAD_OUT_LINE_COLOR = black# 侵入不可エリア枠線
OUT_LINE_COLOR = black      # 枠線の色
YOUR_COLOR = blue           # あなたのユニットの色
ENEMY_COLOR = yellow        # 相手のユニットの色

class Battle(GameSequenceBase):
    class BattleState(Enum):
        Start = 0
        Counter = 1
        Think = 2
        Stop = 3
        Move = 4
        Load = 5
        End = 10

    def __init__(self, pgLib : PgLib) -> None:
        '''コンストラクタ'''
        self.TurnCount = 1
        self.TurnDisplay = TURN_DISPLAY
        self.pgLib = pgLib
        self.map = Map()
        self.player = Player()
        self.enemy = Enemy()
        self.screen = self.pgLib.GetScreen()
        self.counter = MAX_COUNTER * FPS
        self.state = self.BattleState.Start


    def Update(self):
        if self.state == self.BattleState.Start:
            self.state = self.BattleState.Counter
            return
        elif self.state == self.BattleState.Counter:
            self.TurnDisplay -= 1
            self.counter = MAX_COUNTER * FPS
            if self.TurnDisplay == 0:
                self.state = self.BattleState.Think
            else:
                self.state = self.BattleState.Counter
            return
        elif self.state == self.BattleState.Think:
            self.counter -= 1
            if self.counter == 0:
                self.state = self.BattleState.Stop
            return
        elif self.state == self.BattleState.Stop:
            self.TurnCount += 1
            if self.TurnCount == 7:
                self.state = self.BattleState.End
            else:
                self.TurnDisplay = TURN_DISPLAY
                self.state = self.BattleState.Counter
            return


    def Draw(self):
        if self.state == self.BattleState.Start:
            # マップの描画
            self.DrawMap(self.map)
            # プレイヤーの描画
            self.CreatePlayer(self.player)
            # エネミーの描画
            self.CreateEnemy(self.enemy)
        elif self.state == self.BattleState.Counter:
            # マップの描画
            self.DrawMap(self.map)
            # プレイヤーの描画
            self.CreatePlayer(self.player)
            # エネミーの描画
            self.CreateEnemy(self.enemy)
            # ターン経過
            self.DrawTurn()
            # 上部円タイマー
            self.DrawCircleTimer()
            # 数字タイマー
            self.DrawCountTimer()
        elif self.state == self.BattleState.Think:
            # マップの描画
            self.DrawMap(self.map)
            # プレイヤーの描画
            self.CreatePlayer(self.player)
            # エネミーの描画
            self.CreateEnemy(self.enemy)
            # 上部円タイマー
            self.DrawCircleTimer()
            # 数字タイマー
            self.DrawCountTimer()
        elif self.state == self.BattleState.Think:
            # マップの描画
            self.DrawMap(self.map)
            # プレイヤーの描画
            self.CreatePlayer(self.player)
            # エネミーの描画
            self.CreateEnemy(self.enemy)
            # 上部円タイマー
            self.DrawCircleTimer()
            # 数字タイマー
            self.DrawCountTimer()


    def DrawMap(self, map):
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


    def CreatePlayer(self, player):
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


    def CreateEnemy(self, enemy):
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


    def DrawTurn(self):
        if self.TurnDisplay > 20:
            self.Turnfont = pygame.font.Font(None, 100)
            self.Turncounter = self.Turnfont.render( "Turn" + str(self.TurnCount), True, black)
            self.screen.blit(self.Turncounter, [CANVAS_WIDTH / 2 - 70, CANVAS_HEIGHT / 2 - 25])
        else:
            self.Turnfont = pygame.font.Font(None, 100)
            self.Turncounter = self.Turnfont.render( "Start", True, black)
            self.screen.blit(self.Turncounter, [CANVAS_WIDTH / 2 - 70, CANVAS_HEIGHT / 2 - 25])


    def DrawCircleTimer(self):
        pygame.draw.circle(self.screen, yellow, (TIMER_X, TIMER_Y), CIRCLE_WIDTH_OUT)
        pygame.draw.circle(self.screen, red, (TIMER_X, TIMER_Y), CIRCLE_WIDTH_IN)
        pygame.draw.arc(self.screen, green, [TIMER_X - CIRCLE_WIDTH_IN, TIMER_Y - CIRCLE_WIDTH_IN, CIRCLE_WIDTH_IN * 2, CIRCLE_WIDTH_IN * 2], pi/2, (pi/2) + (2*pi) * self.counter / (MAX_COUNTER * FPS), CIRCLE_WIDTH_IN)


    def DrawCountTimer(self):
        self.Timerfont = pygame.font.Font(None, 30)
        count = math.floor(self.counter / FPS)
        self.Timercounter = self.Timerfont.render( str(count), True, black)
        counter_length = len( str(count) )
        #self.screen.blit(self.Timercounter, [TIMER_X - 16, TIMER_Y - 9])               #映らない時用
        if counter_length == 3:
            self.screen.blit(self.Timercounter, [TIMER_X - 16, TIMER_Y - 9])
        elif counter_length == 2:
            self.screen.blit(self.Timercounter, [TIMER_X - 12, TIMER_Y - 9])
        elif counter_length == 1:
            self.screen.blit(self.Timercounter, [TIMER_X - 9, TIMER_Y - 9])
        


#    counter = 100
#    text = font.render(str(counter), True, (0, 128, 0))
#
#    timer_event = pygame.USEREVENT+1
#    pygame.time.set_timer(timer_event, 1000)
#
#    def drawArc(surf, color, center, radius, width, end_angle):
#        arc_rect = pygame.Rect(0, 0, radius*2, radius*2)
#        arc_rect.center = center
#        pygame.draw.arc(surf, color, arc_rect, 0, end_angle, width)
#
#    run = True
#    while run:
#        clock.tick(60)
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                run = False
#            elif event.type == timer_event:
#                counter -= 1
#                text = font.render(str(counter), True, (0, 128, 0))
#                if counter == 0:
#                    pygame.time.set_timer(timer_event, 0)                
#
#        window.fill((255, 255, 255))
#        text_rect = text.get_rect(center = window.get_rect().center)
#        window.blit(text, text_rect)
#        drawArc(window, (255, 0, 0), (100, 100), 90, 10, 2*math.pi*counter/100)
#        pygame.display.flip()


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

