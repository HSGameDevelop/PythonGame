import pygame
from pygame import constants

import sys
sys.path.append('../Util/')
from ..Util.Singleton import Singleton

sys.path.append('../IO/')
from ..IO.InputManager import InputManager

   
class PgLib(Singleton):
    # 初期化(幅・高さ)
    def __init__(self, title : str, width : int, height : int) -> None:
        # ゲーム画面を初期化
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((width, height))
        self.bgColor = (0, 0, 0)

        # 入力管理クラスのインスタンス生成
        self.inputManager = InputManager()

    # スクリーンの取得
    def GetScreen(self):
        return self.screen

    # 入力情報管理インスタンスの取得
    def GetInputManager(self) -> InputManager:
        return self.inputManager
    
    # 背景色の色を設定
    def SetBgColor(self, r, g, b):
        self.bgColor = (r, g, b)

    # ライブラリの更新処理
    def Update(self):
        self.inputManager.Update()

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
        # 終了イベントを確認
        if pygame.event.get(constants.QUIT):
            pygame.quit()
            return True
        
        return False
