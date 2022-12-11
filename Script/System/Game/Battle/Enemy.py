
from .Character import Character
from .BattleDefine import SideType
from ..Data.ColorList import ColorList

class Enemy(Character):
    def __init__(self, xl, yl, num, p_num):
        super().__init__(xl, yl, SideType.Enemy, num + p_num)

    def EnemyDraw(self):
        if self.isVisible == True:
            if self.isSelect == True:
                self.Draw(ColorList.LIGHTYELLOW)
            else:
                self.Draw(ColorList.YELLOW)
        else:
            if self.isSelect == True:
                self.Draw(ColorList.YELLOW)
            else:
                self.Draw(ColorList.OLIVE)
