# 命令クラス
class Command:
    # 初期化
    def __init__(self, func, *args) -> None:
        self.func = func
        self.args = args
        self.isPlay = False

    # コールバック呼び出し
    def Handler(self):
        return self.func(*self.args)

    def SetIsPlay(self, isPlay : bool):
        self.isPlay = isPlay

    def GetIsPlay(self) -> bool:
        return self.isPlay

#命令ベースクラス
class CommandBase:
    def __init__(self) -> None:
        pass
