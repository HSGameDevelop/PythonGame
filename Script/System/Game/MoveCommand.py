import numpy as np
from enum import Enum

from .GameDefine import GameDefine
from .GameObject import GameObject

class Command:
        def __init__(self, func, *args) -> None:
            self.func = func
            self.args = args

        def Handler(self):
            return self.func(*self.args)

class MoveCommand:
    class MoveType(Enum):
        Normal = 0

    def __init__(self) -> None:
        self.commandList : list = []

    def AddCommand(self, type : MoveType, *args):
        if type == MoveCommand.MoveType.Normal:
            self.commandList.append(Command(self.MoveToPosition, *args))

    def DeleteCommand(self, command : Command):
        self.commandList.remove(command)

    def Update(self):
        for command in self.commandList:
            if command.Handler():
                self.commandList.remove(command)
            
    # 指定座標に向かって移動する
    def MoveToPosition(self, gameObject : GameObject, targetPos : GameDefine.Position, moveSpeed : float) -> bool:
        # 現在の座標を取得
        pos = gameObject.GetPos()

        # 不要な計算を省く
        if targetPos.x - pos.x <= moveSpeed and targetPos.y - pos.y <= moveSpeed:
            gameObject.SetPos(targetPos.x, targetPos.y)
            return True

        # 現在の位置から目標の位置までのベクトルを求める
        targetDir = np.array([targetPos.x - pos.x, targetPos.y - pos.y])

        # 内積を求める
        dot = np.dot(GameDefine.DEFAULT_DIRECTION, targetDir)
        
        # ベクトルの長さを計算
        dis = np.linalg.norm(targetDir)
        
        # 角度をラジアンから度に変換
        degree = np.degrees(np.arccos(dot / (GameDefine.DEFAULT_DISTANCE * dis))) 

        # 座標の計算
        x = pos.x + np.cos(degree) * moveSpeed
        y = pos.y + np.sin(degree) * moveSpeed
        
        # 座標の設定
        gameObject.SetPos(x, y)
        
        return False
        
