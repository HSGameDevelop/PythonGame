import pygame
from pygame import display
from pygame import constants
   
class PgLibImpl:
    def __init__(self, width, height) -> None:
        # ゲーム画面を初期化
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.bgColor = (0, 0, 0)

    def GetScreen(self):
        return self.screen
    
    def SetBgColor(self, r, g, b):
        self.bgColor = (r, g, b)

    def DrawStart(self):
        # 背景を黒で塗りつぶす
        self.screen.fill(self.bgColor)

    def DrawEnd(self):
        # 画面を更新
        pygame.display.update()

    def CheckEnd(self) -> bool:
        # 画面を更新
        pygame.display.update()
        # 終了イベントを確認
        for event in pygame.event.get():
            if event.type == constants.QUIT:
                pygame.quit()
                return True

        return False

class PgLib:
    # 初期化(幅・高さを指定する)
    def __init__(self, width, height) -> None:
        self.pgLib = PgLibImpl(width, height)

    # スクリーンの取得
    def GetScreen(self):
        return self.screen

    # 背景色の色を設定
    def SetBgColor(self, r, g, b):
        self.pgLib.SetBgColor(r, g, b)

    # 描画開始
    def DrawStart(self):
        self.pgLib.DrawStart()

    # 描画終了
    def DrawEnd(self):
        self.pgLib.DrawEnd()

    # 終了確認
    def CheckEnd(self) -> bool:
        return self.pgLib.CheckEnd()