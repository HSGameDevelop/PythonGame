from ctypes import resize
import pygame
from pygame import constants

import sys
sys.path.append('../Util/')
from .Singleton import Singleton

sys.path.append('../IO/')
from ..IO.InputManager import InputManager

# pygameのラッパーライブラリの中身
class PgLibImpl(Singleton):
    # 初期化(幅・高さ)
    def __init__(self, title : str, width : int, height : int, fps : int) -> None:
        # ゲーム画面を初期化
        pygame.init()
        pygame.display.set_caption(title)
        pygame.time.Clock().tick(fps)
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

    # 画像のサイズを取得
    def GetImageSize(self, image: pygame.surface):
        return image.get_rect().size
    
    # 画像のリサイズ
    def ResizeImage(self, image : pygame.surface, width : int, height : int):
        imageSize = image.get_rect().size
        imageWidth = imageSize[0]
        imageHeight = imageSize[1]
        if width > 0:
            imageWidth = width
        if height > 0:
            imageHeight = height
        return pygame.transform.scale(image, (imageWidth, imageHeight))

    # 円形の描画
    def DrawCircle(self, color : pygame.color.Color, x : float, y : float, size : float):
        pygame.draw.circle(self.screen, color, (x, y), size)

    # 楕円形の描画
    def DrawEllipse(self, color : pygame.color.Color, x : int, y : int, width : int, height : int):
        pygame.draw.ellipse(self.screen, color, (x, y, width, height))

    # 画像を描画
    def DrawImage(self, image : pygame.surface, x : int, y : int, width : int, height : int):
        # 画像データの設定
        drawImage = self.ResizeImage(image, width, height)

        # 画像サイズの取得
        imageSize = drawImage.get_rect().size

        # 画像の描画
        self.screen.blit(drawImage, (x, y, imageSize[0], imageSize[1]))

    # 画像を分割描画
    def DrawImageSplit(self, image : pygame.surface, rect : tuple[float, float, float, float], imageRect : tuple[float, float, float, float]):
        # 画像の描画
        self.screen.blit(image, rect, imageRect)

    # 画像をスクリーンの中心に表示
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

# pygameのラッパーライブラリの呼び出す部分
pgLib : PgLibImpl = None
class PgLib:
    # 初期化
    @staticmethod
    def Initialize(title : str, width : int, height : int, fps : int):
        global pgLib
        if pgLib == None:
            pgLib = PgLibImpl(title, width, height, fps)

    # インスタンス取得
    @staticmethod
    def GetInstance():
        return pgLib

    # スクリーンの取得
    @staticmethod
    def GetScreen():
        return PgLib.GetInstance().GetScreen()

    # スクリーンのサイズを取得
    @staticmethod
    def GetScreenSize():
        return PgLib.GetInstance().GetScreenSize()

    # スクリーンの中心座標を取得
    @staticmethod
    def GetScreenCenterPos():
        return PgLib.GetInstance().GetScreenCenterPos()

    # 入力情報管理インスタンスの取得
    @staticmethod
    def GetInputManager() -> InputManager:
        return PgLib.GetInstance().GetInputManager()
    
    # 背景色の色を設定
    @staticmethod
    def SetBgColor(r, g, b):
        PgLib.GetInstance().SetBgColor(r, g, b)

    # 画像のサイズを取得
    @staticmethod
    def GetImageSize(image : pygame.surface):
        return PgLib.GetInstance().GetImageSize(image)

    # 画像の読み込み(画像のインスタンスを返す)
    @staticmethod
    def LoadImage( filePath):
        return PgLib.GetInstance().LoadImage(filePath)
    
    # 画像のリサイズ
    @staticmethod
    def ResizeImage(image : pygame.surface, width : int, height : int):
        return PgLib.GetInstance().ResizeImage(image, width, height)

    # 円形を描画
    @staticmethod
    def DrawCircle(color : pygame.color.Color, x : float, y : float, size : float):
        PgLib.GetInstance().DrawCircle(color, x, y, size)

    # 楕円形を描画
    @staticmethod
    def DrawEllipse(color : pygame.color.Color, x : int, y : int, width : int, height : int):
        PgLib.GetInstance().DrawEllipse(color, x, y, width, height)

    # 画像を描画
    @staticmethod
    def DrawImage(image : pygame.surface, x : float, y : float, width : float, height : float):
        PgLib.GetInstance().DrawImage(image, x, y, width, height)

    # 画像を分割描画
    @staticmethod
    def DrawImageSplit(image : pygame.surface, rect : tuple[float, float, float, float], imageRect : tuple[float, float, float, float]):
        PgLib.GetInstance().DrawImageSplit(image, rect, imageRect)

    # 画像をスクリーンの中心に表示
    @staticmethod
    def DrawImageCenter(image : pygame.surface, width : int = 0, height : int = 0):
        PgLib.GetInstance().DrawImageCenter(image, width, height)

    # ライブラリの更新処理
    @staticmethod
    def Update():
        PgLib.GetInstance().Update()

    # 描画開始
    @staticmethod
    def DrawStart():
        PgLib.GetInstance().DrawStart()

    # 描画終了
    @staticmethod
    def DrawEnd():
        PgLib.GetInstance().DrawEnd()

    # 終了確認
    @staticmethod
    def CheckEnd() -> bool:
        return PgLib.GetInstance().CheckEnd()
