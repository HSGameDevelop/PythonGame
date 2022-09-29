import numpy as np
from enum import Enum

from .Define import Define
from .GameObject import GameObject
from .Command import Command

# 移動命令制御クラス
class MoveCommand:
    # 移動の種類
    class MoveType(Enum):
        NormalToPosition = 0

    # 初期化
    def __init__(self) -> None:
        self.commandList : list = []

    # コマンドの追加
    def AddCommand(self, type : MoveType, *args):
        if type == MoveCommand.MoveType.NormalToPosition:
            self.commandList.append(Command(self.MoveToPosition, *args))

    # コマンドの削除
    def DeleteCommand(self, command : Command):
        self.commandList.remove(command)

    # 更新処理
    def Update(self):
        for command in self.commandList:
            if command.Handler():
                self.DeleteCommand(command)
            
    # 指定座標に向かって移動する
    def MoveToPosition(self, gameObject : GameObject, targetPos : Define.Position, moveSpeed : float) -> bool:
        # 現在の座標を取得
        pos = gameObject.GetPos()

        # 不要な計算を省く
        if  abs(targetPos.x - pos.x) <= moveSpeed and abs(targetPos.y - pos.y) <= moveSpeed:
            gameObject.SetPos(targetPos.x, targetPos.y)
            return True

        
        # 現在の位置から目標の位置までのベクトルを求める
        targetDir = np.array([targetPos.x - pos.x, targetPos.y - pos.y])
        # ベクトルの長さを計算
        dis = np.linalg.norm(targetDir)
        normX = targetDir[0] / dis
        normY = targetDir[1] / dis

        # 座標の計算
        x = pos.x + normX * moveSpeed    
        y = pos.y + normY * moveSpeed
        
        # 座標の設定
        gameObject.SetPos(x, y)
        
        return False
        
