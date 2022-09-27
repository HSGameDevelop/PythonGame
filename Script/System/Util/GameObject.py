import numpy as np
import pygame.surface

from Script.Data.ColorList import ColorList
from .PgLib import PgLib
from .Define import Define

# ゲームに使用するオブジェクトのクラス
class GameObject:

##########################
# メソッド
# ########################
    # 初期化
    def __init__(
        self,
        position : tuple[float, float] = (0, 0),
        size : tuple[float, float] = (0, 0),
        direction : tuple[float, float] = (1, 0),
        image : pygame.surface = None,
        moveSpeed : float = 0.0
     ) -> None:
        self.position = Define.Position(position[0], position[1])
        self.size = Define.Size(size[0], size[1])
        self.direction = Define.Direction(direction[0], direction[1])
        self.image : pygame.surface = image

    # 座標の取得
    def GetPos(self) -> Define.Position:
        return self.position

    # 座標の設定
    def SetPos(self, x : float, y : float):
        self.position.x = x
        self.position.y = y

    # サイズの取得
    def GetSize(self) -> Define.Size:
        return self.size

    # サイズの設定
    def SetSize(self, width : float, height: float):
        self.size.width = width
        self.size.height = height

    # 向きの取得
    def GetDir(self) -> Define.Direction:
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

    # 更新
    def Update(self):
        pass

    # 描画
    def Draw(self, color : ColorList = ColorList.WHITE):
        if self.image:
            PgLib.DrawImage(self.image, self.position.x, self.position.y, self.size.width, self.size.height)
        else:
            # 横幅を円のサイズとする
            PgLib.DrawCircle(color.value, self.position.x, self.position.y, self.size.width)
    