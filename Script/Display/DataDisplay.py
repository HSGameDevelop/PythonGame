import numpy as np
import pygame

from Script.Data.ColorList import ColorList
from ..System.Util.PgLib import PgLib
from ..System.Util.Define import Define


# ユニットデータ表示管理
class DataDisplay:

##########################
# メソッド
# ########################
    # 初期化
    def __init__(
        self,
        position : tuple[float, float] = (0, 0),
        size : tuple[float, float] = (0, 0),
        
     ) -> None:
        self.font = pygame.font.Font(None, 15)
        self.position = Define.Position(position[0], position[1])
        self.size = Define.Size(size[0], size[1])


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

    # 更新
    def Update(self):
        pass

    # 描画
    def Draw(self, color : ColorList = ColorList.WHITE):
        # 横幅を円のサイズとする
        PgLib.DrawRect(color.value, self.position.x, self.position.y, self.size.width, self.size.height)
    