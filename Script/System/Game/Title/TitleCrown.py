from enum import Enum
import sys
from turtle import pos

from Script.System.Util.Command.MoveCommand import MoveCommand
from ...Util.Command.CommandUtil import CommandUtil
sys.path.append('../Util/')
from ...Util.GameObject import GameObject 
from ...Util.PgLib import PgLib
from ...Util.Define import Define

class TitleCrown(GameObject):
    TITLE_CROWN_IMAGE_PATH = "Resource/Image/Title/Title_Icon"
    TITLE_CROWN_START_POS = (1170, -200)
    TITLE_CROWN_END_POS = (1170, 350)
    IMAGE_SIZE = 128.0
    IMAGE_NUM_MAX = 7
    IMAGE_NUM_LOOP_START = 4

    class TitleCrownState(Enum):
        Init = 0,
        Move = 1,
        Anim = 2,
        LoopAnim = 3

    def __init__(self) -> None:
        super().__init__(position=TitleCrown.TITLE_CROWN_START_POS, size=(128,128))
        self.timer = 0
        self.state = TitleCrown.TitleCrownState.Init
        
        self.imageNum = 0
        self.oldImageNum = 0
        self.imageList = []
        for i in range(TitleCrown.IMAGE_NUM_MAX):
            self.imageList.append(PgLib.LoadImage(TitleCrown.TITLE_CROWN_IMAGE_PATH + str(i + 1) + ".png"))

        self.SetImage(self.GetNumImage(0))
        self.SetBaseImage(self.GetNumImage(0))

    # 固有の画像取得処理
    def GetNumImage(self, num):
        return self.imageList[num]
        
    def Update(self):
        if self.state == TitleCrown.TitleCrownState.Init:
            CommandUtil.AddMoveCommand(MoveCommand.MoveType.NormalToPosition, self, Define.Position(TitleCrown.TITLE_CROWN_END_POS[0], TitleCrown.TITLE_CROWN_END_POS[1]), startFrame=0, endFrame=30)
            CommandUtil.AddMoveCommand(MoveCommand.MoveType.Rotate, self, angle=-20, startFrame=5, endFrame=25)
            self.state = TitleCrown.TitleCrownState.Move
        elif self.state == TitleCrown.TitleCrownState.Move:
            if self.GetPos().y == TitleCrown.TITLE_CROWN_END_POS[1]:
                self.state = TitleCrown.TitleCrownState.Anim
        elif self.state == TitleCrown.TitleCrownState.Anim:
            self.timer += 1
            if self.timer % 5 == 0:
                self.imageNum += 1
            if self.imageNum >= TitleCrown.IMAGE_NUM_LOOP_START:
                self.state = TitleCrown.TitleCrownState.LoopAnim
        elif self.state == TitleCrown.TitleCrownState.LoopAnim:
            self.timer += 1
            if self.timer % 3 == 0:
                if self.imageNum < TitleCrown.IMAGE_NUM_MAX - 1:
                    self.imageNum += 1
                else:
                    self.imageNum = TitleCrown.IMAGE_NUM_LOOP_START

        self.SetBaseImage(self.GetNumImage(self.imageNum))
