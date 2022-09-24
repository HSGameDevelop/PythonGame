from .Singleton import Singleton
from .MoveCommand import MoveCommand

# 命令制御クラスの中身
class CommandUtilImpl(Singleton):
    def __init__(self) -> None:
        self.moveCommand : MoveCommand = MoveCommand()
    
    def AddMoveCommand(self, type : MoveCommand.MoveType, *args):
        self.moveCommand.AddCommand(type, *args)

    def Update(self):
        self.moveCommand.Update()

# 命令制御クラスの呼び出す部分
commandUtil : CommandUtilImpl = None
class CommandUtil:
    @staticmethod
    def Initialize():
        global commandUtil
        commandUtil = CommandUtilImpl()

    @staticmethod
    def GetInstance():
        return commandUtil

    @staticmethod
    def AddMoveCommand(type : MoveCommand.MoveType, *args):
        CommandUtil.GetInstance().AddMoveCommand(type, *args)

    @staticmethod
    def Update():
        CommandUtil.GetInstance().Update()

    
