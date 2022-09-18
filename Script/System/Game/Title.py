import sys
from .GameSequenceBase import GameSequenceBase
from .PgLib import PgLib
import pygame

TITLE_IMAGE_DIRECTORY = "Resource/Image/Title/"
TITLE_BG = "test_bg.jpg"
TITLE_LOGO = "TitleLogo.png"
TITLE_ICON_BLADE = "Icon_Blade.png"

ICON_MOVE_SPEED = 10
class Title(GameSequenceBase):
    def __init__(self, pgLib : PgLib) -> None:
        #画像の読み込み
        self.bgImage = pgLib.LoadImage(TITLE_IMAGE_DIRECTORY + TITLE_BG)
        self.Logo = pgLib.LoadImage(TITLE_IMAGE_DIRECTORY + TITLE_LOGO)
        self.bladeImage = pgLib.LoadImage(TITLE_IMAGE_DIRECTORY + TITLE_ICON_BLADE)

        # アイコンのリサイズ
        self.bladeImage = pgLib.ResizeImage(self.bladeImage, 128, 128)
        self.bladeX = 0
        self.bladeY = 390
        self.bladeEndX = 890

        self.pgLib = pgLib

    def Update(self):
        if self.bladeX < self.bladeEndX:
            self.bladeX += ICON_MOVE_SPEED
        pass

    def Draw(self):
        screen = self.pgLib.GetScreen()

        # 背景の描画
        screen.blit(self.bgImage, (0, 0, 1280, 960))
         # 武器アイコンを表示
        screen.blit(self.bladeImage, (self.bladeX, self.bladeY))
        # タイトルロゴの描画(中心に配置)
        self.pgLib.DrawImageCenter(self.Logo, 960, 720)

       