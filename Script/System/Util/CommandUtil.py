from Script.System.Util.GameObject import GameObject
from .Singleton import Singleton
from .MoveCommand import MoveCommand
from .Define import Define

# 命令制御クラスの中身
class CommandUtilImpl(Singleton):
    # 初期化
    def __init__(self) -> None:
        self.moveCommand : MoveCommand = MoveCommand()
    
    # 移動命令の追加
    def AddMoveCommand(self, type : MoveCommand.MoveType, *args):
        self.moveCommand.AddCommand(type, *args)

    # 更新処理
    def Update(self):
        self.moveCommand.Update()

# 命令制御クラスの呼び出す部分
commandUtil : CommandUtilImpl = None
class CommandUtil:
    # 初期化
    @staticmethod
    def Initialize():
        global commandUtil
        if commandUtil == None:
            commandUtil = CommandUtilImpl()

    # インスタンス取得
    @staticmethod
    def GetInstance():
        return commandUtil

    # 移動命令の追加
    @staticmethod
    def AddMoveCommand(type : MoveCommand.MoveType, gameObject : GameObject, pos : Define.Position, moveSpeed : float):
        CommandUtil.GetInstance().AddMoveCommand(type, *(gameObject, pos, moveSpeed))

    # 更新処理
    @staticmethod
    def Update():
        CommandUtil.GetInstance().Update()

    
