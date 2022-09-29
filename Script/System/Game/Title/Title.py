import sys
from enum import Enum
from turtle import pos

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
TITLE_ICON_BLADE = "Icon_Blade.png"

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
        self.crown = TitleCrown()

        # ステートの初期化
        self.state : Title.TitleState = Title.TitleState.Start

    # 更新処理
    def Update(self) -> bool:
        if self.state == Title.TitleState.Start:
            self.state = Title.TitleState.LogoIn
        elif self.state == Title.TitleState.LogoIn:
            self.crown.Update()
            # 剣アイコン移動
            CommandUtil.Update()

            if PgLib.GetInputManager().GetMouse().GetPushClick() != None:
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

        # タイトルロゴの描画(中心に配置)
        PgLib.DrawImageCenter(self.Logo)

        # 王冠の描画
        self.crown.Draw()
        

       