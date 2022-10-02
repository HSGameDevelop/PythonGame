import sys
from enum import Enum
from turtle import pos

import pygame
import numpy as np

from Script.System.IO.InputKeyboard import InputKeyboard
from ..GameSequenceBase import GameSequenceBase

sys.path.append('../Util/')
from ...Util.PgLib import PgLib
from ...Util.MoveCommand import MoveCommand
from ...Util.CommandUtil import CommandUtil
from ...Util.Define import Define
from ...Util.GameObject import GameObject

from .TitleCrown import TitleCrown

TITLE_IMAGE_DIRECTORY = "Resource/Image/Title/"
TITLE_BG = "Title_Bg.png"
TITLE_LOGO = "Title_Logo.png"
TITLE_TEXT = "Title_Text.png"
TITLE_ASHIATO = "Title_Ashiato.png"

BLADE_ROGO_POS = Define.Position(890, 390)


ICON_MOVE_SPEED = 30
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
        self.text = PgLib.LoadImage(TITLE_IMAGE_DIRECTORY + TITLE_TEXT)
        self.ashiato = PgLib.LoadImage(TITLE_IMAGE_DIRECTORY + TITLE_ASHIATO)
        self.crown = TitleCrown()

        # text用
        self.count = 0
        self.textAlpha = 0

        # 足跡用
        self.height = 0
        self.size = PgLib.GetImageSize(self.ashiato)

        # ステートの初期化
        self.state : Title.TitleState = Title.TitleState.Start

    # 更新処理
    def Update(self) -> bool:
        # 初期化
        if self.state == Title.TitleState.Start:
            self.state = Title.TitleState.LogoIn

        # ロゴ表示
        elif self.state == Title.TitleState.LogoIn:
            self.crown.Update()
        
            if PgLib.GetInputManager().GetMouse().GetPushClick() != None:
                self.state = Title.TitleState.Run

        # 更新
        elif self.state == Title.TitleState.Run:
            self.state = Title.TitleState.End
        
        # 終了処理
        elif self.state == Title.TitleState.End:
            return True        

        self.count += 2
        self.textAlpha = (np.sin(-np.pi/2+np.pi/120*self.count)+1)/2 * 255
        self.height = (np.sin(-np.pi/2+np.pi/120*(self.count * 0.5))+1)/2 * self.size[1]
        
        return False

    def Draw(self):
        screen = PgLib.GetScreen()
        # 背景の描画
        screen.blit(self.bgImage, (0, 0, 1280, 960))

        # タイトルロゴの描画(中心に配置)
        size = PgLib.GetImageSize(self.Logo)
        PgLib.DrawImage(self.Logo, 900 - size[0] / 2, 400 - size[1] / 2, size[0], size[1])

        pygame.Surface.set_alpha(self.text, self.textAlpha, 0)
        PgLib.DrawImage(self.text, 400 - 320, 820 - 32, 640, 64)

        PgLib.DrawImageSplit(self.ashiato, (264 - self.size[0] / 2, 320 - self.size[1] / 2, self.size[0], self.size[1]), (0, 0, self.size[0], self.size[1]))

        # 王冠の描画
        self.crown.Draw()
        

       