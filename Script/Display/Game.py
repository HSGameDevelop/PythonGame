import sys, os
sys.path.append('../../Script/Display/')
from Script.Display.GameDraw import GameDraw

sys.path.append('../../Script/System/')
from Script.System.PgLib import PgLib

sys.path.append('../../Script/System/IO/')
from Script.System.IO.InputManager import InputManager

WIDTH = 640
HEIGHT = 480

# ゲーム全般を扱うクラス
class Game:    
    def __init__(self):
        self.pgLib = PgLib(WIDTH, HEIGHT)
        #self.tkIntance = tkIntance
        #self.gd = GameDraw(self.tkIntance)
        #self.inputManager = InputManager(tkIntance)
        return

    # ゲーム全般の更新処理
    def Update(self):
        #gameUpdate.Update()
        return

    # ゲーム全般の描画処理
    def Draw(self):
        # 描画開始
        self.pgLib.DrawStart()

        #gameDraw.Update()

        # 描画終了
        self.pgLib.DrawEnd()
        return

    # ゲームの終了確認
    def CheckEnd(self) -> bool:
        return self.pgLib.CheckEnd()