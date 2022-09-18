import sys, os
import pygame

sys.path.append('../../System/')
from Script.System.Game.PgLib import PgLib
from Script.System.Game.Title import Title

WIDTH = 1280
HEIGHT = 960
GAME_TITLE = "ActKing"

# ゲーム全般を扱うクラス
class Game:    
    def __init__(self):
        self.pgLib = PgLib(GAME_TITLE, WIDTH, HEIGHT)
        self.gameSequence = Title(self.pgLib)

    # ゲーム全般の更新処理
    def Update(self):
        self.pgLib.Update()
        self.gameSequence.Update()

        # キー入力確認用
        pushKey = self.pgLib.GetInputManager().GetKeyboard().GetPushKey()
        if pushKey:
            print("Push Key : ", pygame.key.name(pushKey))

    # ゲーム全般の描画処理
    def Draw(self):
        # 描画開始
        self.pgLib.DrawStart()

        self.gameSequence.Draw()

        # 描画終了
        self.pgLib.DrawEnd()

    # ゲームの終了確認
    def CheckEnd(self) -> bool:
        return self.pgLib.CheckEnd()