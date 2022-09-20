import sys
from enum import Enum

from Script.System.IO.InputKeyboard import InputKeyboard
from .GameSequenceBase import GameSequenceBase
from .PgLib import PgLib
import pygame

TITLE_IMAGE_DIRECTORY = "Resource/Image/Title/"
TITLE_BG = "test_bg.jpg"
TITLE_LOGO = "TitleLogo.png"
TITLE_ICON_BLADE = "Icon_Blade.png"



ICON_MOVE_SPEED = 10
class Title(GameSequenceBase):
    class TitleState(Enum):
        Start = 0
        LogoIn = 1
        Run = 2
        End = 3

    def __init__(self) -> None:
        #画像の読み込み
        self.bgImage = PgLib.LoadImage(TITLE_IMAGE_DIRECTORY + TITLE_BG)
        self.Logo = PgLib.LoadImage(TITLE_IMAGE_DIRECTORY + TITLE_LOGO)
        self.bladeImage = PgLib.LoadImage(TITLE_IMAGE_DIRECTORY + TITLE_ICON_BLADE)

        # アイコンのリサイズ
        self.bladeImage = PgLib.ResizeImage(self.bladeImage, 128, 128)
        self.bladeX = -100
        self.bladeY = 390
        self.bladeEndX = 890

        # ステートの初期化
        self.state : Title.TitleState = Title.TitleState.Start

    # 更新処理
    def Update(self):

        if self.state == Title.TitleState.Start:
            self.state = Title.TitleState.LogoIn
            return
        elif self.state == Title.TitleState.LogoIn:
            if self.bladeX < self.bladeEndX:
                self.bladeX += ICON_MOVE_SPEED
            
            if PgLib.GetInputManager().GetKeyboard().GetPushKey():
                self.bladeX = self.bladeEndX
                self.state = Title.TitleState.Run
            return
        elif self.state == Title.TitleState.Run:
            self.state = Title.TitleState.LogoIn
            return
        elif self.state == Title.TitleState.End:
            return

    def Draw(self):
        screen = PgLib.GetScreen()

        # 背景の描画
        screen.blit(self.bgImage, (0, 0, 1280, 960))
         # 武器アイコンを表示
        screen.blit(self.bladeImage, (self.bladeX, self.bladeY))
        # タイトルロゴの描画(中心に配置)
        PgLib.DrawImageCenter(self.Logo, 960, 720)

       