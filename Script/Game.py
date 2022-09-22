import sys, os
import pygame
from Script.System.Game.GameSequenceBase import GameSequenceBase

sys.path.append('../../System/')
from Script.System.Game.PgLib import PgLib
from Script.System.Game.Title import Title
sys.path.append('../../Display/')
from Script.Display.Battle import Battle

WIDTH = 1280
HEIGHT = 960
FPS = 60
GAME_TITLE = "ActKing"

# ゲーム全般を扱うクラス
class Game:    
    def __init__(self):
        PgLib.Initialize(GAME_TITLE, WIDTH, HEIGHT, FPS)
        
        self.gameSequence : GameSequenceBase = Title()
        #self.gameSequence : GameSequenceBase = Battle()

    # ゲーム全般の更新処理
    def Update(self):
        PgLib.Update()
        if self.gameSequence.Update():
            self.gameSequence = Battle()

        # キー入力確認用
        pushKey = PgLib.GetInputManager().GetKeyboard().GetPushKey()
        if pushKey:
            print("Push Key : ", pygame.key.name(pushKey))
        
    # ゲーム全般の描画処理
    def Draw(self):
        # 描画開始
        PgLib.DrawStart()

        self.gameSequence.Draw()
        # 描画終了
        PgLib.DrawEnd()
                

    # ゲームの終了確認
    def CheckEnd(self) -> bool:
        return PgLib.CheckEnd()