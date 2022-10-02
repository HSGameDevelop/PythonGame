
from .Singleton import Singleton

# タイマークラス
class Timer:
    # 初期化
    def __init__(self, key : str) -> None:
        self.frameCount = 0
        self.key = key

    # キーの取得
    def GetKey(self) -> str:
        return self.key

    # 現在の経過フレームを取得
    def GetFrameCount(self) -> int:
        return self.frameCount

    # 計測フレームに指定した値を加算する
    def AddFrameCount(self, addFrame : int = 1):
        self.frameCount += addFrame

# タイマー管理クラスの処理実装クラス
class TimerManagerImpl(Singleton):
    # 初期化
    def __init__(self) -> None:
        self.timerList : list = []

    # タイマーを追加する
    def AddTimer(self, key : str, frame : int, func):
        self.timerList.append({"timer" : Timer(key), "frame" : frame, "func" : func})

    # タイマーを消去する
    def RemoveTimer(self, key : str):
        for timer in self.timerList:
            if timer["timer"].GetKey() == key:
                self.timerList.remove(timer)
                break

    # 更新処理
    def Update(self):
        for timer in self.timerList:
            timer["timer"].AddFrameCount()
            if timer["timer"].GetFrameCount() >= timer["frame"]:
                timer["func"]()
                self.RemoveTimer(timer["timer"].GetKey())

# タイマー管理クラスの呼び出しクラス
timerManager : TimerManagerImpl = None 
class TimerManager:
    # 初期化
    @staticmethod
    def Initialize():
        global timerManager
        if timerManager == None:
            timerManager = TimerManagerImpl()

    # インスタンス取得
    @staticmethod
    def GetInstance() -> TimerManagerImpl:
        return timerManager

    # タイマーを追加する
    @staticmethod
    def AddTimer(key : str, frame : int, func):
        TimerManager.GetInstance().AddTimer(key, frame, func)

    # タイマーを消去する
    @staticmethod
    def RemoveTimer(key : str):
        TimerManager.GetInstance().RemoveTimer(key)

    # 更新処理
    @staticmethod
    def Update():
        TimerManager.GetInstance().Update()
