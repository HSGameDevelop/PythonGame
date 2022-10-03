from tracemalloc import start
from Script.System.Util.Command import Command
from Script.System.Util.GameObject import GameObject
from .Singleton import Singleton
from .MoveCommand import MoveCommand
from .Define import Define
from .Timer import TimerManager

# 命令制御クラスの中身
class CommandUtilImpl(Singleton):
    # 初期化
    def __init__(self) -> None:
        self.moveCommand : MoveCommand = MoveCommand()
        self.id = 0
        self.frameCount = 0
        self.commandList : list = [ ] # Command
    
    # 移動命令の追加
    def AddMoveCommand(self, type : MoveCommand.MoveType, gameObject : GameObject, pos : Define.Position, angle : float, startFrame, endFrame):
        command = self.moveCommand.GetCommand(type, gameObject, pos, angle, endFrame)
        if command != None:
            self.commandList.append(command)
            def CommandPlay():
                command.SetIsPlay(True)
            TimerManager.AddTimer(str(self.id), startFrame, CommandPlay)

    # 更新処理
    def Update(self):
        for command in self.commandList:
            if command.GetIsPlay():
                    if command.Handler():
                        self.commandList.remove(command)

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
    def AddMoveCommand(type : MoveCommand.MoveType, gameObject : GameObject, pos : Define.Position = Define.Position(0.0, 0.0), angle : float = 0.0, startFrame : int = 0, endFrame : int = 1):
        CommandUtil.GetInstance().AddMoveCommand(type, gameObject, pos, angle, startFrame, endFrame)

    # 更新処理
    @staticmethod
    def Update():
        CommandUtil.GetInstance().Update()

    
