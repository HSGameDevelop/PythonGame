from enum import Enum
import sys
from turtle import pos

from Script.System.Util.MoveCommand import MoveCommand
sys.path.append('../Util/')
from ...Util.GameObject import GameObject 
from ...Util.PgLib import PgLib
from ...Util.CommandUtil import CommandUtil

TITLE_CROWN_IMAGE_PATH = "Resource/Image/Title/Title_Icon.png"
TITLE_CROWN_START_POS = (780, -200)
TITLE_CROWN_END_POS = (780, 480)

class TitleCrown(GameObject):
    class TitleCrownState(Enum):
        Init = 0,
        Move = 1,
        Anim = 2,
        LoopAnim = 3

    def __init__(self) -> None:
        super().__init__(image=PgLib.LoadImage(TITLE_CROWN_IMAGE_PATH), position=TITLE_CROWN_START_POS)
        self.state = TitleCrown.TitleCrownState.Init

    def Update(self):
        if self.state == TitleCrown.TitleCrownState.Init:
            CommandUtil.AddMoveCommand(MoveCommand.MoveType.NormalToPosition, self, TITLE_CROWN_END_POS, 16)
            self.state = TitleCrown.TitleCrownState.Move
            return
        elif self.state == TitleCrown.TitleCrownState.Move:
            if self.GetPos().y == TITLE_CROWN_END_POS[1]:
                self.state = TitleCrown.TitleCrownState.Anim
            return
        elif self.state == TitleCrown.TitleCrownState.Anim:
            self.state = TitleCrown.TitleCrownState.LoopAnim
            return
        elif self.state == TitleCrown.TitleCrownState.LoopAnim:
            return
                

