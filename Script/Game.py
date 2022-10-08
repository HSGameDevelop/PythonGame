from distutils.cmd import Command
import sys, os
import pygame
from Script.System.Game.GameSequenceBase import GameSequenceBase

from .System.Game.Battle.Battle import Battle

from .System.Game.Data.GameData import GameData
from .System.Util.PgLib import PgLib
from .System.Util.Timer import TimerManager
sys.path.append('./System/Util/Command')
from .System.Util.Command.CommandUtil import CommandUtil
sys.path.append('./System/Game/Title/')
from .System.Game.Title.Title import Title

WIDTH = 1280
HEIGHT = 960
FPS = 60
GAME_TITLE = "ActKing"

# ゲーム全般を扱うクラス
class Game:    
    def __init__(self):
        PgLib.Initialize(GAME_TITLE, WIDTH, HEIGHT, FPS)
        TimerManager.Initialize()
        CommandUtil.Initialize()
        GameData.Initialize()
        
        self.gameSequence : GameSequenceBase = Title()
        #self.gameSequence : GameSequenceBase = Battle()

    # ゲーム全般の更新処理
    def Update(self):
        PgLib.Update()
        TimerManager.Update()
        CommandUtil.Update()
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