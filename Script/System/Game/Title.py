import sys
from .GameSequenceBase import GameSequenceBase
from .PgLib import PgLib
import pygame



class Title(GameSequenceBase):
    def __init__(self, pgLib : PgLib) -> None:
        #画像の読み込み
        self.bgImage = pgLib.LoadImage("Resource/Image/test_bg.jpg")
        self.Logo = pgLib.LoadImage("Resource/Image/TitleLogo.png")
        self.pgLib = pgLib

    def Update(self):
        pass

    def Draw(self):
        screen = self.pgLib.GetScreen()

        # 背景の描画
        screen.blit(self.bgImage, (0, 0, 1280, 960))
        # タイトルロゴの描画(中心に配置)
        self.pgLib.DrawImageCenter(self.Logo)