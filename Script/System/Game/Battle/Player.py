from .Character import Character
from .BattleDefine import SideType
from ..Data.ColorList import ColorList

class Player(Character):
    def __init__(self, xl, yl, num):
        super().__init__(xl, yl, SideType.Player, num)
        self.__visibleArea : list = []
        self.__moveArea : list = []

    def PlayerDraw(self):
        if self.IsVisible == True:
            if self.IsSelect == True:
                self.Draw(ColorList.LIGHTBLUE)
            else:
                self.Draw(ColorList.BLUE)
        else:
            if self.IsSelect == True:
                self.Draw(ColorList.BLUE)
            else:
                self.Draw(ColorList.DARKBLUE)

    @property
    def VisibleArea(self):
        return self.__visibleArea
    @VisibleArea.setter
    def VisibleArea(self, visibleArea):
        self.__visibleArea = visibleArea

    @property
    def MoveArea(self):
        return self.__moveArea
    @MoveArea.setter
    def MoveArea(self, moveArea):
        self.__moveArea = moveArea

