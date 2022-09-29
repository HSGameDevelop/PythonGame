from enum import Enum
import sys
from turtle import pos

from Script.System.Util.MoveCommand import MoveCommand
sys.path.append('../Util/')
from ...Util.GameObject import GameObject 
from ...Util.PgLib import PgLib
from ...Util.CommandUtil import CommandUtil
from ...Util.Define import Define

class TitleCrown(GameObject):
    TITLE_CROWN_IMAGE_PATH = "Resource/Image/Title/Title_Icon.png"
    TITLE_CROWN_START_POS = (1160, -200)
    TITLE_CROWN_END_POS = (1160, 350)
    IMAGE_SIZE = 128.0
    IMAGE_NUM_MAX = 6 # ０からの計算
    IMAGE_NUM_LOOP_START = 4

    class TitleCrownState(Enum):
        Init = 0,
        Move = 1,
        Anim = 2,
        LoopAnim = 3

    def __init__(self) -> None:
        super().__init__(image=PgLib.LoadImage(TitleCrown.TITLE_CROWN_IMAGE_PATH), position=TitleCrown.TITLE_CROWN_START_POS, size=(128,128))
        self.imageNum = 0
        self.timer = 0
        self.state = TitleCrown.TitleCrownState.Init

    def Update(self):
        if self.state == TitleCrown.TitleCrownState.Init:
            CommandUtil.AddMoveCommand(MoveCommand.MoveType.NormalToPosition, self, Define.Position(TitleCrown.TITLE_CROWN_END_POS[0], TitleCrown.TITLE_CROWN_END_POS[1]), 16)
            self.state = TitleCrown.TitleCrownState.Move
        elif self.state == TitleCrown.TitleCrownState.Move:
            if self.GetPos().y == TitleCrown.TITLE_CROWN_END_POS[1]:
                self.state = TitleCrown.TitleCrownState.Anim
        elif self.state == TitleCrown.TitleCrownState.Anim:
            self.timer += 1
            if self.timer % 6 == 0:
                self.imageNum += 1
            if self.imageNum >= TitleCrown.IMAGE_NUM_LOOP_START:
                self.state = TitleCrown.TitleCrownState.LoopAnim
        elif self.state == TitleCrown.TitleCrownState.LoopAnim:
            self.timer += 1
            if self.timer % 3 == 0:
                self.imageNum += 1
            if self.imageNum > TitleCrown.IMAGE_NUM_MAX:
                self.imageNum = TitleCrown.IMAGE_NUM_LOOP_START
         
    def Draw(self):
        pos = self.GetPos()
        size = self.GetSize()
        PgLib.DrawImageSplit(self.GetImage(), (pos.x, pos.y, size.width, size.height), (self.imageNum * TitleCrown.IMAGE_SIZE, 0, TitleCrown.IMAGE_SIZE, TitleCrown.IMAGE_SIZE))
