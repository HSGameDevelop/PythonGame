
from .BattleDefine import *
from .CharanterManager import CharacterManager

class BattleUtil:
    
    ##
    # @fn __init__()
    # @brief 初期化処理
    # @return なし
    def __init__(self) -> None:
        self.__characterManager = CharacterManager()

    ##
    # @fn CreateCharacterFromStageId(int)
    # @brief 指定されたステージIDに応じてキャラクターを生成する
    # @param [in] stageId ステージのID
    # @return なし
    def CreateCharacterFromStageId(self, stageId : int):
        # 現状は完全ランダムでよい
        charaCount : int = 6
        for i in range(charaCount):
            self.CharacterManager.CreateCharacter(CharacterType.Player)
            self.CharacterManager.CreateCharacter(CharacterType.Enemy)

    @property
    def CharacterManager(self):
        return self.__characterManager

