from .Character import Character
from .BattleDefine import SideType
from ..Data.ColorList import ColorList

class Player(Character):
    def __init__(self, xl, yl, num):
        super().__init__(xl, yl, SideType.Player, num)

    def PlayerDraw(self):
        if self.isVisible == True:
            if self.isSelect == True:
                self.Draw(ColorList.LIGHTBLUE)
            else:
                self.Draw(ColorList.BLUE)
        else:
            if self.isSelect == True:
                self.Draw(ColorList.BLUE)
            else:
                self.Draw(ColorList.DARKBLUE)