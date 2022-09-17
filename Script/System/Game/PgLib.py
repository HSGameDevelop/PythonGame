import pygame
from pygame import constants

import sys
sys.path.append('/Script/System/Game/')
from Script.System.Game.Singleton import Singleton
   
class PgLib(Singleton):
    # 初期化(幅・高さ)
    def __init__(self, width, height) -> None:
        # ゲーム画面を初期化
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.bgColor = (0, 0, 0)

    # スクリーンの取得
    def GetScreen(self):
        return self.screen
    
    # 背景色の色を設定
    def SetBgColor(self, r, g, b):
        self.bgColor = (r, g, b)

    # 描画開始
    def DrawStart(self):
        # 背景を黒で塗りつぶす
        self.screen.fill(self.bgColor)

    # 描画終了
    def DrawEnd(self):
        # 画面を更新
        pygame.display.update()

    # 終了確認
    def CheckEnd(self) -> bool:
        # 画面を更新
        pygame.display.update()
        # 終了イベントを確認
        for event in pygame.event.get():
            if event.type == constants.QUIT:
                pygame.quit()
                return True

        return False
