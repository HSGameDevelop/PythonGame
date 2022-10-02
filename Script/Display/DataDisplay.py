import numpy as np
import pygame

from Script.Data.ColorList import ColorList
from ..System.Util.PgLib import PgLib
from ..System.Util.Define import Define

FONT_PATH = "./Data/FontData/ipaexg.ttf"

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
        self.position = Define.Position(position[0], position[1])
        self.size = Define.Size(size[0], size[1])
        self.font_padding = 10
        self.outline = 10
        self.font_size1 = None
        self.font_size2 = None
        self.font_size3 = None
        self.font_size4 = None
        self.font_size5 = None
        self.font_size6 = None
        self.font_size7 = None
        self.font_size8 = None
        self.font_size9 = None
        self.font_size10 = None
        self.font1 = None
        self.font2 = None
        self.font3 = None
        self.font4 = None
        self.font5 = None
        self.font6 = None
        self.font7 = None
        self.font8 = None
        self.font9 = None
        self.font10 = None
        self.text1 = None
        self.text2 = None
        self.text3 = None
        self.text4 = None
        self.text5 = None
        self.text6 = None
        self.text7 = None
        self.text8 = None
        self.text9 = None
        self.text10 = None
        self.screen = PgLib.GetScreen()

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

    def GetText1(self):
        return self.text1

    def SetText1(self, text1):
        self.text1 = text1

    def GetText2(self):
        return self.text2

    def SetText2(self, text2):
        self.text2 = text2

    def GetText3(self):
        return self.text3

    def SetText3(self, text3):
        self.text3 = text3

    def GetText4(self):
        return self.text4

    def SetText4(self, text4):
        self.text4 = text4

    def GetText5(self):
        return self.text5

    def SetText5(self, text5):
        self.text5 = text5

    def GetText6(self):
        return self.text6

    def SetText6(self, text6):
        self.text6 = text6

    def GetText7(self):
        return self.text7

    def SetText7(self, text7):
        self.text7 = text7

    def GetText8(self):
        return self.text8

    def SetText8(self, text8):
        self.text8 = text8

    def GetText9(self):
        return self.text9

    def SetText9(self, text9):
        self.text9 = text9

    def GetText10(self):
        return self.text10

    def SetText10(self, text10):
        self.text10 = text10

    def GetFontsize1(self):
        return self.font_size1

    def SetFontsize1(self, font_size1):
        self.font_size1 = font_size1

    def GetFontsize2(self):
        return self.font_size2

    def SetFontsize2(self, font_size2):
        self.font_size2 = font_size2

    def GetFontsize3(self):
        return self.font_size3

    def SetFontsize3(self, font_size3):
        self.font_size3 = font_size3

    def GetFontsize4(self):
        return self.font_size4

    def SetFontsize4(self, font_size4):
        self.font_size4 = font_size4

    def GetFontsize5(self):
        return self.font_size5

    def SetFontsize5(self, font_size5):
        self.font_size5 = font_size5

    def GetFontsize6(self):
        return self.font_size6

    def SetFontsize6(self, font_size6):
        self.font_size6 = font_size6

    def GetFontsize7(self):
        return self.font_size7

    def SetFontsize7(self, font_size7):
        self.font_size7 = font_size7

    def GetFontsize8(self):
        return self.font_size8

    def SetFontsize8(self, font_size8):
        self.font_size8 = font_size8

    def GetFontsize9(self):
        return self.font_size9

    def SetFontsize9(self, font_size9):
        self.font_size9 = font_size9

    def GetFontsize10(self):
        return self.font_size10

    def SetFontsize10(self, font_size10):
        self.font_size10 = font_size10

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
        if self.font_size1 != None:
            self.font1 = pygame.font.Font(FONT_PATH, self.font_size1)
            text1 = self.font1.render(self.text1, True, color3.value)
            self.screen.blit(text1, [self.position.x + self.font_padding, self.position.y + self.font_padding])
        if self.font_size2 != None:
            self.font2 = pygame.font.Font(FONT_PATH, self.font_size2)
            text2 = self.font2.render(self.text2, True, color3.value)
            self.screen.blit(text2, [self.position.x + self.font_padding, self.position.y + self.font_size1 + (self.font_padding*2)])
        if self.font_size3 != None:
            self.font3 = pygame.font.Font(FONT_PATH, self.font_size3)
            text3 = self.font3.render(self.text3, True, color3.value)
            self.screen.blit(text3, [self.position.x + self.font_padding, self.position.y + self.font_size1 + self.font_size2 + (self.font_padding*3)])
        if self.font_size4 != None:
            self.font4 = pygame.font.Font(FONT_PATH, self.font_size4)
            text4 = self.font4.render(self.text4, True, color3.value)
            self.screen.blit(text4, [self.position.x + self.font_padding, self.position.y + self.font_size1 + self.font_size2 + self.font_size3 + (self.font_padding*4)])
        if self.font_size5 != None:
            self.font5 = pygame.font.Font(FONT_PATH, self.font_size5)
            text5 = self.font5.render(self.text5, True, color3.value)
            self.screen.blit(text5, [self.position.x + self.font_padding, self.position.y + self.font_size1 + self.font_size2 + self.font_size3 + self.font_size4 + (self.font_padding*5)])
        if self.font_size6 != None:
            self.font6 = pygame.font.Font(FONT_PATH, self.font_size6)
            text6 = self.font6.render(self.text6, True, color3.value)
            self.screen.blit(text6, [self.position.x + self.font_padding, self.position.y + self.font_size1 + self.font_size2 + self.font_size3 + self.font_size4 + self.font_size5 + (self.font_padding*6)])
        if self.font_size7 != None:
            self.font7 = pygame.font.Font(FONT_PATH, self.font_size7)
            text7 = self.font7.render(self.text7, True, color3.value)
            self.screen.blit(text7, [self.position.x + self.font_padding, self.position.y + self.font_size1 + self.font_size2 + self.font_size3 + self.font_size4 + self.font_size5 + self.font_size6 + (self.font_padding*7)])
        if self.font_size8 != None:
            self.font8 = pygame.font.Font(FONT_PATH, self.font_size8)
            text8 = self.font8.render(self.text8, True, color3.value)
            self.screen.blit(text8, [self.position.x + self.font_padding, self.position.y + self.font_size1 + self.font_size2 + self.font_size3 + self.font_size4 + self.font_size5 + self.font_size6 + self.font_size7 + (self.font_padding*8)])
        if self.font_size9 != None:
            self.font9 = pygame.font.Font(FONT_PATH, self.font_size9)
            text9 = self.font9.render(self.text9, True, color3.value)
            self.screen.blit(text9, [self.position.x + self.font_padding, self.position.y + self.font_size1 + self.font_size2 + self.font_size3 + self.font_size4 + self.font_size5 + self.font_size6 + self.font_size7 + self.font_size8 + (self.font_padding*9)])
        if self.font_size10 != None:
            self.font10 = pygame.font.Font(FONT_PATH, self.font_size10)
            text10 = self.font10.render(self.text10, True, color3.value)
            self.screen.blit(text10, [self.position.x + self.font_padding, self.position.y + self.font_size1 + self.font_size2 + self.font_size3 + self.font_size4 + self.font_size5 + self.font_size6 + self.font_size7 + self.font_size8 + self.font_size9 + (self.font_padding*10)])




        #text = font.render(self.text, True, color3.value)
        #self.screen.blit(text, [pos.x  - 8, pos.y])