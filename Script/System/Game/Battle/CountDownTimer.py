import pygame
import time
from math import pi
import math
from ...Util.PgLib import PgLib
# カラーリスト
from ..Data.ColorList import ColorList

CIRCLE_WIDTH_OUT = 40
CIRCLE_WIDTH_IN = 35
FPS = 60

class CountDownTimer():
    def __init__(self, start, x, y):
        """スタートはフレーム数"""
        self.screen = PgLib.GetScreen()             # スクリーンの設定
        self.start = start              # 初期値（変更しない）
        self.counter = start            # 毎フレーム引いていく
        self.x = x
        self.y = y
        # 時間計測開始
        self.time_sta = time.perf_counter()

    def Update(self):
        # 時間計測更新（フレーム毎）
        time_end = time.perf_counter()
        # 経過時間（秒）
        tim = time_end- self.time_sta
        self.counter = self.start - tim

    def Draw(self, circle_color : ColorList = ColorList.WHITE, move_circle_color : ColorList = ColorList.WHITE, out_color : ColorList = ColorList.WHITE, font_color : ColorList = ColorList.WHITE):
        self.Timer(circle_color,out_color)
        self.MoveTimer(move_circle_color)
        self.CountFont(font_color)

    def GetCounter(self):
        return self.counter

    def SetCounter(self, counter):
        self.counter = counter

    def Timer(self, circle_color, out_color):
        """ここは固定されている時計の土台"""
        pygame.draw.circle(self.screen, out_color.value, (self.x, self.y), CIRCLE_WIDTH_OUT)
        pygame.draw.circle(self.screen, circle_color.value, (self.x, self.y), CIRCLE_WIDTH_IN)

    def CountFont(self, font_color):
        self.Timerfont = pygame.font.Font(None, 30)
        counter = math.ceil(self.counter)
        self.Timercounter = self.Timerfont.render( str(counter), True, font_color.value)
        counter_length = len( str(counter) )
        #self.screen.blit(self.Timercounter, [x - 16, y - 9])               #映らない時　用
        # 文字をなるべくタイマーの中央寄せにするため下の処理
        if counter_length == 6:
            self.screen.blit(self.Timercounter, [self.x - 27, self.y - 9])
        elif counter_length == 5:
            self.screen.blit(self.Timercounter, [self.x - 23, self.y - 9])
        elif counter_length == 4:
            self.screen.blit(self.Timercounter, [self.x - 20, self.y - 9])
        if counter_length == 3:
            self.screen.blit(self.Timercounter, [self.x - 16, self.y - 9])
        elif counter_length == 2:
            self.screen.blit(self.Timercounter, [self.x - 12, self.y - 9])
        elif counter_length == 1:
            self.screen.blit(self.Timercounter, [self.x - 9, self.y - 9])

    def MoveTimer(self, move_circle_color):
        pygame.draw.arc(self.screen, move_circle_color.value, [self.x - CIRCLE_WIDTH_IN, self.y - CIRCLE_WIDTH_IN, CIRCLE_WIDTH_IN * 2, CIRCLE_WIDTH_IN * 2], pi/2,  (pi/2) + (2*pi)  * (self.counter * 0.98) / self.start, CIRCLE_WIDTH_IN)

