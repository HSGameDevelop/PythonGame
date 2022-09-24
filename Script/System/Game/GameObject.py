import pygame.surface

from Script.Data.ColorList import ColorList
from .PgLib import PgLib

# ゲームに使用するオブジェクトのクラス
class GameObject:
##########################
# パラメータ用クラス
# ########################    
    # 座標
    class Position:
        def __init__(self, x : int = 0, y : int = 0) -> None:
            self.x = x
            self.y = y

    # サイズ
    class Size:
        def __init__(self, width : int = 0, height : int = 0) -> None:
            self.width = width
            self.height = height

    # 向き
    class Direction:
        def __init__(self, x : int = 0, y : int = 0) -> None:
            self.x = x
            self.y = y

##########################
# メソッド
# ########################
    # 初期化
    def __init__(self, position : tuple[int, int] = (0, 0), size : tuple[int, int] = (0, 0), direction : tuple[int, int] = (0, 0), image : pygame.surface = None) -> None:
        self.position = GameObject.Position(position[0], position[1])
        self.size = GameObject.Size(size[0], size[1])
        self.direction = GameObject.Direction(direction[0], direction[1])
        self.image : pygame.surface = image

    # 座標の取得
    def GetPos(self) -> Position:
        return self.position

    # 座標の設定
    def SetPos(self, x : int, y : int):
        self.position.x = x
        self.position.y = y

    # サイズの取得
    def GetSize(self) -> Size:
        return self.size

    # サイズの設定
    def SetSize(self, width : int, height: int):
        self.size.width = width
        self.size.height = height

    # 向きの取得
    def GetDir(self) -> Direction:
        return self.direction
    
    # 向きの設定
    def SetDir(self, x, y):
        self.direction.x = x
        self.direction.y = y

    # 画像の取得
    def GetImage(self) -> pygame.surface:
        return self.image

    # 画像の設定
    def SetImage(self, image : pygame.surface):
        self.image = image

    # 描画
    def Draw(self):
        if self.image:
            PgLib.DrawImage(self.image, self.position.x, self.position.y, self.size.width, self.size.height)
        else:
            PgLib.DrawEllipse(ColorList.WHITE, self.position.x, self.position.y, self.size.width, self.size.height)
    