import sys, os
sys.path.append('../../Script/System/IO/')
from Script.System.IO.InputKeyboard import InputKeyboard

# 入力管理クラス
class InputManager:
    # 初期化
    def __init__(self) -> None:
        self.intputKeyboard = InputKeyboard()

    # 入力情報の更新処理
    def Update(self):
        self.intputKeyboard.Update()
