from ctypes import resize
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

    # スクリーンのサイズを取得
    def GetScreenSize(self):
        return self.screen.get_rect().size

    # スクリーンの中心座標を取得
    def GetScreenCenterPos(self):
        screenSize = self.screen.get_rect().size
        return (screenSize[0] / 2, screenSize[1] / 2)

    # 入力情報管理インスタンスの取得
    def GetInputManager(self) -> InputManager:
        return self.inputManager
    
    # 背景色の色を設定
    def SetBgColor(self, r, g, b):
        self.bgColor = (r, g, b)

    # 画像の読み込み(画像のインスタンスを返す)
    def LoadImage(self, filePath):
        return pygame.image.load(filePath)
    
    # 画像のリサイズ
    def ResizeImage(self, image : pygame.surface, width : int, height : int):
        imageSize = image.get_rect().size
        imageWidth = imageSize[0]
        imageHeight = imageSize[1]
        if width > 0 :
            imageWidth = width
        if height > 0:
            imageHeight = height
        return pygame.transform.scale(image, (imageWidth, imageHeight))

    # 画像をスクリーンの中心に表示する
    def DrawImageCenter(self, image : pygame.surface, width : int = 0, height : int = 0):
        # 画像データの設定
        drawImage = self.ResizeImage(image, width, height)
        
        # 中心座標の計算
        imageSize = drawImage.get_rect().size
        screenSize = self.screen.get_rect().size
        x = screenSize[0] / 2 - imageSize[0] / 2
        y = screenSize[1] / 2 - imageSize[1] / 2
        w = screenSize[0] / 2 + imageSize[0] / 2
        h = screenSize[1] / 2 + imageSize[1] / 2
        
        # 画像の描画
        self.screen.blit(drawImage, (x, y, w, h))

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
