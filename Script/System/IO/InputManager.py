import sys, os

sys.path.append('../Util/')
from ..Util.Singleton import Singleton

sys.path.append('../IO/')
from ..IO.InputKeyboard import InputKeyboard
from ..IO.InputMouse import InputMouse

# 入力管理クラス
class InputManager(Singleton):
    # 初期化
    def __init__(self) -> None:
        self.intputKeyboard = InputKeyboard()
        self.intputMouse = InputMouse()

    # 入力情報の更新処理
    def Update(self):
        self.intputKeyboard.Update()
        self.intputMouse.Update()

    # キーボードの入力管理インスタンスを取得
    def GetKeyboard(self) -> InputKeyboard:
        return self.intputKeyboard

    # キーボードの入力管理インスタンスを取得
    def GetMouse(self) -> InputMouse:
        return self.intputMouse