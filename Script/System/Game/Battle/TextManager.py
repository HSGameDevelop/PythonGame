import numpy as np
import pygame

from ..Data.ColorList import ColorList
from ...Util.PgLib import PgLib
from ...Util.Define import Define

FONT_PATH = "./Data/FontData/ipaexg.ttf"

# ユニットデータ表示管理
class TextManager:

##########################
# メソッド
# ########################
    # 初期化
    def __init__(
        self,
        position : tuple[float, float] = (0, 0),
        size : tuple[float, float] = (0, 0),
     ) -> None:
        self.position = Define.Position(position[0], position[1])
        self.size = Define.Size(size[0], size[1])
        self.screen = PgLib.GetScreen()
        self.font_padding = 10
        self.outline = 10
        self.font_size = []
        self.font = []
        self.text = []
        self.font_num = None
        

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

    def GetText(self):
        return self.text

    def SetText(self, text):
        self.text = text

    def GetFontsize(self):
        return self.font_size

    def SetFontsize(self, font_size):
        self.font_size = font_size

    def GetFontNum(self):
        return self.font_num

    def SetFontNum(self, font_num):
        self.font_num = font_num

    # 更新
    def Update(self):
        pass

    # 描画
    def Draw(self, color1 : ColorList = ColorList.WHITE, color2 : ColorList = ColorList.WHITE, color3 : ColorList = ColorList.WHITE):
        # 内部の色
        PgLib.DrawRect(color1.value, self.position.x, self.position.y, self.size.width, self.size.height, 0)
        # 大外の枠
        PgLib.DrawRect(color2.value, self.position.x, self.position.y, self.size.width, self.size.height, self.outline)
        # テキスト
        if self.font_size != None:
            self.font = pygame.font.Font(FONT_PATH, self.font_size)
            text = self.font.render(self.text, True, color3.value)
            self.screen.blit(text, [self.position.x + self.font_padding, self.position.y + self.font_padding])

        #text = font.render(self.text, True, color3.value)
        #self.screen.blit(text, [pos.x  - 8, pos.y])