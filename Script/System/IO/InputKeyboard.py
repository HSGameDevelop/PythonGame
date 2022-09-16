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

    def KeyPush(self, e):
        self.key = e.keysym
    
    def KeyPop(self, e):
        self.key = None

    def GetPushKey(self):
        return self.key

    def CheckPushKey(self, key):
        return self.GetPushKey() == key
