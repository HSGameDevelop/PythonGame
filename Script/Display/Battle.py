from enum import Enum
import time
import pygame
from pygame.locals import *
from math import pi
import math
import sys, os
# マップ表示のクラス
from .Map import Map
# プレイヤー表示のクラス
from .Character import Character, Player, Enemy
sys.path.append('../../System/Game/')
from Script.System.Game.PgLib import PgLib
from Script.System.Game.GameSequenceBase import GameSequenceBase
from Script.System.IO.InputKeyboard import InputKeyboard
from Script.System.IO.InputMouse import InputMouse
# カラーリスト
sys.path.append('../../Data/')
from Script.Data.ColorList import ColorList

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

MINUS1 = (MAX_COUNTER * FPS) / 90

# 色の設定
BOARD_COLOR = ColorList.GRAY.value              # 盤面全体（見えない位置）
VISIBLE_COLOR = ColorList.WHITE.value           # ユニットから見える範囲（カラー）
DEAD_COLOR = ColorList.MAROON.value             # 侵入不可エリア
DEAD_OUT_LINE_COLOR = ColorList.BLACK.value     # 侵入不可エリア枠線
OUT_LINE_COLOR = ColorList.BLACK.value          # 枠線の色
YOUR_COLOR = ColorList.BLUE.value               # あなたのユニットの色
ENEMY_COLOR = ColorList.YELLOW.value            # 相手のユニットの色


class Battle(GameSequenceBase):
    class BattleState(Enum):
        Start = 0
        Counter = 1
        Think = 2
        Stop = 3
        Move = 4
        Load = 5
        End = 10


    def __init__(self) -> None:
        '''コンストラクタ'''
        self.TurnCount = 1                          # ターンのカウント
        self.TurnDisplay = TURN_DISPLAY             # ターンの表示時間
        self.map = Map()                            # Map管理
        self.player = Player()                      # Playerユニット
        self.enemy = Enemy()                        # Enemyユニット
        self.screen = PgLib.GetScreen()             # スクリーンの設定
        self.counter = MAX_COUNTER * FPS            # シーン「Think」の時間設定
        self.state = self.BattleState.Start         # バトルのステイト
        self.click_flag_counter = 10                # クリックのフラグが立っている間受付拒否時間
        self.click_flag = False                     # クリックした時のフラグ
        self.pushClick = None                       # クリックしたイベントの取得
        self.before_pushClick = None                # 1つ前のクリックイベントの取得


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
            # キー入力取得期間
            self.counter -= 1
            if self.click_flag == True:
                self.click_flag_counter -= 1
            if self.click_flag_counter == 0:
                self.click_flag = False
                self.click_flag_counter = 10
            if self.counter == -1:
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
            # マウスチェック
            self.UnitData(self.player, self.enemy)


    def DrawMap(self, map):
        # ６点指定 六角形 30*24
        for num in range(720):
            # y = map.m_xy[num][1]   x = map.m_xy[num][0]
            if map.m_xy[num][14] == -1:
                color = DEAD_COLOR
                outline = DEAD_OUT_LINE_COLOR
            elif map.m_xy[num][14] == 0:
                color = BOARD_COLOR
                outline = OUT_LINE_COLOR
            elif map.m_xy[num][14] == 1:
                color = BOARD_COLOR
                outline = OUT_LINE_COLOR
            elif map.m_xy[num][14] == 2:
                color = BOARD_COLOR
                outline = OUT_LINE_COLOR
            elif map.m_xy[num][14] == 3:
                color = BOARD_COLOR
                outline = OUT_LINE_COLOR
            elif map.m_xy[num][14] == 4:
                color = BOARD_COLOR
                outline = OUT_LINE_COLOR


            # 内側描画
            pygame.draw.polygon( self.screen, color, [(map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][4], map.m_xy[num][5]), (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][8], map.m_xy[num][9]), (map.m_xy[num][10], map.m_xy[num][11]), (map.m_xy[num][12], map.m_xy[num][13])])
            # 枠線描画
            pygame.draw.polygon( self.screen, outline, [(map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][4], map.m_xy[num][5]), (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][8], map.m_xy[num][9]), (map.m_xy[num][10], map.m_xy[num][11]), (map.m_xy[num][12], map.m_xy[num][13])], 1)

            if map.m_xy[num][14] == 1:
                pygame.draw.line( self.screen, outline, (map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][8], map.m_xy[num][9]), 2)
                pygame.draw.line( self.screen, outline, (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][12], map.m_xy[num][13]), 2)
            elif map.m_xy[num][14] == 2:
                pygame.draw.line( self.screen, outline, (map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][8], map.m_xy[num][9]), 4)
                pygame.draw.line( self.screen, outline, (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][12], map.m_xy[num][13]), 4)
            elif map.m_xy[num][14] == 3:
                pygame.draw.line( self.screen, outline, (map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][8], map.m_xy[num][9]), 6)
                pygame.draw.line( self.screen, outline, (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][12], map.m_xy[num][13]), 6)
            elif map.m_xy[num][14] == 4:
                pygame.draw.line( self.screen, outline, (map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][8], map.m_xy[num][9]), 8)
                pygame.draw.line( self.screen, outline, (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][12], map.m_xy[num][13]), 8)


    def CreatePlayer(self, player):
        for num in range(6):
            font = pygame.font.Font(None, 15)
            #[num, self.xl[num], self.yl[num], xc, yc, tagname]
            pygame.draw.circle(self.screen, ColorList.BLUE.value, (player.xy[num][3], player.xy[num][4]), 20)
            #self.screen.create_oval(player.xy[num][3], player.xy[num][4], player.xy[num][5], player.xy[num][6], fill=YOUR_COLOR)
            tag_length = len(player.xy[num][5])
            if tag_length == 6:
                text = font.render(player.xy[num][5], True, (255,255,255))
                self.screen.blit(text, [player.xy[num][3] - 10, player.xy[num][4]])
            elif tag_length == 7:
                text = font.render(player.xy[num][5], True, (255,255,255))
                self.screen.blit(text, [player.xy[num][3] - 14, player.xy[num][4]])


    def CreateEnemy(self, enemy):
        for num in range(6):
            font = pygame.font.Font(None, 15)
            #[num, self.xl[num], self.yl[num], xc, yc, tagname]
            pygame.draw.circle(self.screen, ColorList.YELLOW.value, (enemy.xy[num][3], enemy.xy[num][4]), 20)
            #self.screen.create_oval(enemy.xy[num][3], enemy.xy[num][4], enemy.xy[num][5], enemy.xy[num][6], fill=ENEMY_COLOR)
            tag_length = len(enemy.xy[num][5])
            if tag_length == 5:
                text = font.render(enemy.xy[num][5], True, (255,0,0))
                self.screen.blit(text, [enemy.xy[num][3] - 8, enemy.xy[num][4]])
            elif tag_length == 6:
                text = font.render(enemy.xy[num][5], True, (255,0,0))
                self.screen.blit(text, [enemy.xy[num][3] - 10, enemy.xy[num][4]])


    def DrawTurn(self):
        if self.TurnDisplay > 20:
            self.Turnfont = pygame.font.Font(None, 100)
            self.Turncounter = self.Turnfont.render( "Turn" + str(self.TurnCount), True, ColorList.BLACK.value)
            self.screen.blit(self.Turncounter, [CANVAS_WIDTH / 2 - 70, CANVAS_HEIGHT / 2 - 25])
        else:
            self.Turnfont = pygame.font.Font(None, 100)
            self.Turncounter = self.Turnfont.render( "Start", True, ColorList.BLACK.value)
            self.screen.blit(self.Turncounter, [CANVAS_WIDTH / 2 - 70, CANVAS_HEIGHT / 2 - 25])


    def DrawCircleTimer(self):
        pygame.draw.circle(self.screen, ColorList.YELLOW.value, (TIMER_X, TIMER_Y), CIRCLE_WIDTH_OUT)
        pygame.draw.circle(self.screen, ColorList.RED.value, (TIMER_X, TIMER_Y), CIRCLE_WIDTH_IN)
        pygame.draw.arc(self.screen, ColorList.LIME.value, [TIMER_X - CIRCLE_WIDTH_IN, TIMER_Y - CIRCLE_WIDTH_IN, CIRCLE_WIDTH_IN * 2, CIRCLE_WIDTH_IN * 2], pi/2, (pi/2) + (2*pi) * (self.counter * 0.98) / (MAX_COUNTER * FPS), CIRCLE_WIDTH_IN)


    def DrawCountTimer(self):
        self.Timerfont = pygame.font.Font(None, 30)
        count = math.ceil(self.counter / FPS)
        self.Timercounter = self.Timerfont.render( str(count), True, ColorList.BLACK.value)
        counter_length = len( str(count) )
        #self.screen.blit(self.Timercounter, [TIMER_X - 16, TIMER_Y - 9])               #映らない時用
        if counter_length == 3:
            self.screen.blit(self.Timercounter, [TIMER_X - 16, TIMER_Y - 9])
        elif counter_length == 2:
            self.screen.blit(self.Timercounter, [TIMER_X - 12, TIMER_Y - 9])
        elif counter_length == 1:
            self.screen.blit(self.Timercounter, [TIMER_X - 9, TIMER_Y - 9])


    def UnitData(self, player, enemy):
        Point_x, Point_y = PgLib.GetInputManager().GetMouse().GetPosMouce()
        self.pushClick = PgLib.GetInputManager().GetMouse().GetPushClick()
        if self.pushClick != self.before_pushClick:
            if  self.click_flag == False:
                # キー入力確認用
                print("Push Click :  x:", str(Point_x) + " y:" + str(Point_y))
                #font = pygame.font.Font(None, 15)
                #[num, self.xl[num], self.yl[num], xc, yc, tagname]
                if Point_x != None and Point_y !=  None:
                    for p_num in range(6):
                        p_x = math.floor(player.xy[p_num][3])
                        p_y = math.floor(player.xy[p_num][4])
                        if p_x - 21 < Point_x and Point_x < p_x + 21 and p_y - 21 < Point_y and Point_y < p_y + 21:
                            print(player.xy[p_num])

                    for e_num in range(6):
                        e_x = math.floor(enemy.xy[e_num][3])
                        e_y = math.floor(enemy.xy[e_num][4])
                        if e_x - 21 < Point_x and Point_x < e_x + 21 and e_y - 21 < Point_y and Point_y < e_y + 21:
                            print(enemy.xy[e_num])

                self.click_flag = True
                self.before_pushClick = PgLib.GetInputManager().GetMouse().GetPushClick()


    def CalcReturnPos(self, player, enemy):
        # 全部マップ・プレイヤー・エネミー何をクリックしても返ってきます。
        Point_x, Point_y = PgLib.GetInputManager().GetMouse().GetPosMouce()
        self.pushClick = PgLib.GetInputManager().GetMouse().GetPushClick()
        if self.pushClick != self.before_pushClick:
            if  self.click_flag == False:
                # キー入力確認用
                print("Push Click :  x:", str(Point_x) + " y:" + str(Point_y))
                #font = pygame.font.Font(None, 15)
                #[num, self.xl[num], self.yl[num], xc, yc, tagname]
                if Point_x != None and Point_y !=  None:
                    for p_num in range(6):
                        p_x = math.floor(player.xy[p_num][3])
                        p_y = math.floor(player.xy[p_num][4])
                        if p_x - 21 < Point_x and Point_x < p_x + 21 and p_y - 21 < Point_y and Point_y < p_y + 21:
                            print(player.xy[p_num])

                    for e_num in range(6):
                        e_x = math.floor(enemy.xy[e_num][3])
                        e_y = math.floor(enemy.xy[e_num][4])
                        if e_x - 21 < Point_x and Point_x < e_x + 21 and e_y - 21 < Point_y and Point_y < e_y + 21:
                            print(enemy.xy[e_num])

                self.click_flag = True
                self.before_pushClick = PgLib.GetInputManager().GetMouse().GetPushClick()


    def MoveData(self):
        # リストでそれぞれの行動データを生成
        # list = [player or enemy, unit_id, action_number(行動番号), kinds(攻撃・移動・防御(auto)), consumption(行動力消費量), x, y(移動先(今いる場所)), weapon_direction(武器向き), weapon(武器), shield_direction(盾向き), shield(盾)]
        pass


    def MoveUnit(self, move, unit):
        pass
        # 行動数の減り方は、攻撃方法や移動で異なる
        # 行動終了時のplayer or enemy .xy[num][1, 2]に移動先のデータを入れ替え
        # 移動時の計算も必要

