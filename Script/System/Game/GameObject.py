import numpy as np
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
        def __init__(self, x : float = 0, y : float = 0) -> None:
            self.x = x
            self.y = y

    # サイズ
    class Size:
        def __init__(self, width : float = 0, height : float = 0) -> None:
            self.width = width
            self.height = height

    # 向き
    class Direction:
        def __init__(self, x : float = 0, y : float = 0) -> None:
            self.x = x
            self.y = y

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
        self.position = GameObject.Position(position[0], position[1])
        self.size = GameObject.Size(size[0], size[1])
        self.direction = GameObject.Direction(direction[0], direction[1])
        self.image : pygame.surface = image
        self.moveSpeed = moveSpeed

    # 座標の取得
    def GetPos(self) -> Position:
        return self.position

    # 座標の設定
    def SetPos(self, x : float, y : float):
        self.position.x = x
        self.position.y = y

    # サイズの取得
    def GetSize(self) -> Size:
        return self.size

    # サイズの設定
    def SetSize(self, width : float, height: float):
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

    # 移動速度の取得
    def GetMoveSpeed(self) -> float:
        return self.moveSpeed

    # 移動速度の設定
    def SetMoveSpeed(self, moveSpeed : float):
        self.moveSpeed = moveSpeed

    # 更新
    def Update(self):
        if self.moveSpeed > 0.0:
            # 内積を求める
            defaultDir = np.array([1, 0])
            dir = np.array([self.direction.x, self.direction.y]) 
            dot = np.dot(defaultDir, dir)
            
            # ベクトルの長さを計算
            defaultDis = np.linalg.norm(defaultDir)
            dis = np.linalg.norm(dir)
            
            # 角度をラジアンから度に変換
            degree = np.degrees(np.arccos(dot / (defaultDis * dis))) 

            # 座標の計算
            pos = self.GetPos()
            x = pos.x + np.cos(degree) * self.moveSpeed
            y = pos.y + np.sin(degree) * self.moveSpeed

            self.SetPos(x, y)


    # 描画
    def Draw(self):
        if self.image:
            PgLib.DrawImage(self.image, self.position.x, self.position.y, self.size.width, self.size.height)
        else:
            PgLib.DrawEllipse(ColorList.WHITE, self.position.x, self.position.y, self.size.width, self.size.height)
    