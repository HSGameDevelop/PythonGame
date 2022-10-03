import numpy as np
from enum import Enum

from Script.System.Util.PgLib import PgLib

from .Define import Define
from .GameObject import GameObject
from .Command import Command, CommandBase

# 移動命令制御クラス
class MoveCommand(CommandBase):
    # 移動の種類
    class MoveType(Enum):
        NormalToPosition = 0
        Rotate = 1

    # 初期化
    def __init__(self) -> None:
        pass

    # 指定フレームで目標に到達するまでの速度を求める
    def ClacSpeed(self, pos, targetPos, endFrame) -> float:
        # 現在の位置から目標の位置までのベクトルを求める
        targetDir = np.array([targetPos.x - pos.x, targetPos.y - pos.y])
        # ベクトルの長さを計算
        dis = np.linalg.norm(targetDir)
        # 1フレームあたりの移動すべき量を求める
        return dis / endFrame

    # 指定フレームで目標の角度回転するための角度を求める
    def ClacAngle(self, gameObject : GameObject, angle : float, endFrame : int):
        nowAngle = gameObject.GetAngle()
        return (angle - nowAngle) / endFrame

    # コマンドの追加
    def GetCommand(self, type : MoveType, gameObject : GameObject, pos : Define.Position, angle : float, endFrame : int):
        if type == MoveCommand.MoveType.NormalToPosition: # 指定座標に向かって移動
            moveSpeed = self.ClacSpeed(gameObject.GetPos(), pos, endFrame)
            return Command(self.MoveToPosition, *(gameObject, pos, moveSpeed))
        elif type == MoveCommand.MoveType.Rotate: # 指定の角度回転
            rotateAngle = self.ClacAngle(gameObject, angle, endFrame)
            return Command(self.RotateAngle, *(gameObject, rotateAngle, angle))
        return None
            
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
    
    # 指定の角度回転する
    def RotateAngle(self, gameObject : GameObject, angle : float, endAngle : float):
        # 回転が終了しているかどうかの確認
        if abs(gameObject.GetAngle() - endAngle) <= abs(angle):
            # 角度を設定
            nowAngle = gameObject.GetAngle()
            nowAngle += gameObject.GetAngle() - endAngle
            gameObject.SetAngle(nowAngle)
            return True
        
        # 角度を設定
        nowAngle = gameObject.GetAngle()
        nowAngle += angle
        gameObject.SetAngle(nowAngle)

        return False
        
