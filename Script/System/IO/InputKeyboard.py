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
        for event in pygame.event.get():
            if event.type == constants.KEYDOWN: # キーを押した時
                self.key = event.key
            elif event.type == constants.KEYUP: # キーを離した時
                self.key = None

    # 現在押しているキーを取得する
    def GetPushKey(self):
        return self.key

    # 現在押しているキーが指定したキーかどうかを返す(true:押している/false:押していない)
    def CheckPushKey(self, key : InputKeyList):
        return self.GetPushKey() == key
