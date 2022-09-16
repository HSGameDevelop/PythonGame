from enum import Enum
import tkinter

class InputKeyboard:
    class InputKeyList(Enum):
        Up = 'up'
        Left = 'Left'
        Right = 'Right'
        Donw = 'Down'

    def __init__(self, tkInstance : tkinter) -> None:
        self.key = None
        
        tkInstance.bind('<KeyPress>', self.KeyPush)
        tkInstance.bind('<KeyRelease>', self.KeyPop)

    # キーを押下時の処理
    def KeyPush(self, e):
        self.key = e.keysym
    
    # キーを離した時の処理
    def KeyPop(self, e):
        self.key = None

    # 現在押しているキーを取得する
    def GetPushKey(self):
        return self.key

    # 現在押しているキーが指定したキーかどうかを返す(true:押している/false:押していない)
    def CheckPushKey(self, key : InputKeyList):
        return self.GetPushKey() == key
