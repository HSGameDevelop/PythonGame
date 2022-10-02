
from .Singleton import Singleton

# タイマークラス
class Timer:
    def __init__(self, key : str) -> None:
        self.frameCount = 0
        self.key = key

    def GetKey(self) -> str:
        return self.key

    def GetFrameCount(self) -> int:
        return self.frameCount

    def AddFrameCount(self, addFrame : int = 1):
        self.frameCount += addFrame

class TimerManagerImpl(Singleton):
    def __init__(self) -> None:
        self.timerList : list = []

    def AddTimer(self, key : str, frame : int, func):
        self.timerList.append({"timer" : Timer(key), "frame" : frame, "func" : func})

    def RemoveTimer(self, key : str):
        for timer in self.timerList:
            if timer["timer"].GetKey() == key:
                self.timerList.remove(timer)
                break

    def Update(self):
        for timer in self.timerList:
            timer["timer"].AddFrameCount()
            if timer["timer"].GetFrameCount() >= timer["frame"]:
                timer["func"]()
                self.RemoveTimer(timer["timer"].GetKey())

timerManager : TimerManagerImpl = None 
class TimerManager:
    @staticmethod
    def Initialize():
        global timerManager
        if timerManager == None:
            timerManager = TimerManagerImpl()

    @staticmethod
    def GetInstance() -> TimerManagerImpl:
        return timerManager

    @staticmethod
    def AddTimer(key : str, frame : int, func):
        TimerManager.GetInstance().AddTimer(key, frame, func)

    @staticmethod
    def RemoveTimer(key : str):
        TimerManager.GetInstance().RemoveTimer(key)

    @staticmethod
    def Update():
        TimerManager.GetInstance().Update()

    

    