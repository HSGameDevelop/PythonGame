# 命令クラス
class Command:
    # 初期化
    def __init__(self, func, *args) -> None:
        self.func = func
        self.args = args

    # コールバック呼び出し
    def Handler(self):
        return self.func(*self.args)

#命令ベースクラス
class CommandBase:
    def __init__(self) -> None:
        pass
