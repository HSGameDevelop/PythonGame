from enum import Enum
import pygame
from pygame import constants

# キー入力管理クラス
class InputKeyboard:
    class InputKeyList(Enum):
        Up = constants.K_UP
        Left = constants.K_LEFT
        Right = constants.K_RIGHT
        Donw = constants.K_DOWN

    # 初期化
    def __init__(self) -> None:
        self.key = None
        
    # キーボードの情報の更新処理
    def Update(self):
        event = pygame.event.get(constants.KEYDOWN) # キーを押した時
        if event:
            self.key = event[0].key
        elif pygame.event.get(constants.KEYUP): # キーを離した時
            self.key = None
 
    # 現在押しているキーを取得する
    def GetPushKey(self):
        return self.key

    # 現在押しているキーが指定したキーかどうかを返す(true:押している/false:押していない)
    def CheckPushKey(self, key : InputKeyList) -> bool:
        return self.GetPushKey() == key
