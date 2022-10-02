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
     ) -> None:
        self.position = Define.Position(position[0], position[1])
        self.size = Define.Size(size[0], size[1])
        self.direction = Define.Direction(direction[0], direction[1])
        self.image : pygame.surface = image
        self.oldAngle = 0.0
        self.angle = 0.0

        # サイズが設定されていないなら画像のサイズで設定する
        if self.image != None:
            selfSize = self.GetSize()
            if(selfSize.width == 0 and selfSize.height == 0):
                size = PgLib.GetImageSize(self.image)
                self.SetSize(size[0], size[1])

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

    # 角度の取得
    def GetAngle(self) -> float:
        return self.angle

    # 角度の設定
    def SetAngle(self, angle : float):
        self.angle = angle

    # 更新
    def Update(self):
        angle = self.GetAngle()
        if self.oldAngle != angle:
            self.SetImage(PgLib.RotateImage(self.GetImage(), self.oldAngle - angle))
            self.oldAngle = self.GetAngle()

    # 描画
    def Draw(self, color : ColorList = ColorList.WHITE):
        pos = self.GetPos()
        size = self.GetSize()
        if self.image:
            PgLib.DrawImage(self.image, pos.x - size.width / 2, pos.y - size.height / 2, size.width, size.height)
        else:
            # 横幅を円のサイズとする
            PgLib.DrawCircle(color.value, self.position.x, self.position.y, self.size.width)
    