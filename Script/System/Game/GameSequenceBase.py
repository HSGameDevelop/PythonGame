from abc import ABCMeta, abstractmethod

# ゲームの流れのベース(各シーンはこれを継承して実装する)
class GameSequenceBase(metaclass=ABCMeta):
    # 初期化
    @abstractmethod
    def __init__(self) -> None:
        pass

    # 更新処理
    @abstractmethod
    def Update(self):
        pass

    # 描画処理
    @abstractmethod
    def Draw(self):
        pass