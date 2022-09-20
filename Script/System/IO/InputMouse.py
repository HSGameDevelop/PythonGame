from enum import Enum
import pygame
from pygame import constants

# キー入力管理クラス
class InputMouse:
    class InputClickList(Enum):
        Left = constants.BUTTON_LEFT
        Center = constants.BUTTON_MIDDLE
        Right = constants.BUTTON_RIGHT
        Up = constants.BUTTON_WHEELUP
        Down = constants.BUTTON_WHEELDOWN
    
    # 初期化
    def __init__(self) -> None:
        self.click = None
        self.pos = []
        
    # Mouseの情報の更新処理
    def Update(self):
        event = pygame.event.get(constants.MOUSEBUTTONDOWN) # キーを押した時
        if event:
            self.click = event[0].button
            self.pos = event.pos
        elif pygame.event.get(constants.MOUSEBUTTONUP): # キーを離した時
            self.click = None
            self.pos = None
            if pygame.event.get(constants.MOUSEMOTION): #マウス追跡
                self.pos = event.pos
 
    # マウスクリックを取得する
    def GetPushClick(self):
        return self.click
    
    # マウスの位置を取得する
    def GetPosMouce(self):
        return self.pos

    # 現在押しているキーが指定したキーかどうかを返す(true:押している/false:押していない)
    def CheckPushClick(self, click : InputClickList) -> bool:
        return self.GetPushClick() == click
