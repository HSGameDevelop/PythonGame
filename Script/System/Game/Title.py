import sys
from enum import Enum
from turtle import pos

from Script.System.IO.InputKeyboard import InputKeyboard
from .GameSequenceBase import GameSequenceBase
from .PgLib import PgLib
from .GameObject import GameObject
import pygame

TITLE_IMAGE_DIRECTORY = "Resource/Image/Title/"
TITLE_BG = "Title_Bg.png"
TITLE_LOGO = "Title_Logo.png"
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
        self.blade = GameObject(size=(128, 128) , image=PgLib.LoadImage(TITLE_IMAGE_DIRECTORY + TITLE_ICON_BLADE), moveSpeed=ICON_MOVE_SPEED, position=(-100, 390))

        # アイコンのリサイズ
        self.bladeEndX = 890

        # ステートの初期化
        self.state : Title.TitleState = Title.TitleState.Start

    # 更新処理
    def Update(self) -> bool:

        if self.state == Title.TitleState.Start:
            self.state = Title.TitleState.LogoIn
        elif self.state == Title.TitleState.LogoIn:
            if self.blade.GetPos().x < self.bladeEndX:
                self.blade.Update()

            if PgLib.GetInputManager().GetMouse().GetPushClick() != None:
                self.blade.SetMoveSpeed(0.0)
                self.blade.SetPos(self.bladeEndX , 390)
                self.state = Title.TitleState.Run
        elif self.state == Title.TitleState.Run:
            self.state = Title.TitleState.End
        elif self.state == Title.TitleState.End:
            return True
        
        return False

    def Draw(self):
        screen = PgLib.GetScreen()
        # 背景の描画
        screen.blit(self.bgImage, (0, 0, 1280, 960))
        # 武器アイコンを表示
        self.blade.Draw()
        # タイトルロゴの描画(中心に配置)
        PgLib.DrawImageCenter(self.Logo)

       