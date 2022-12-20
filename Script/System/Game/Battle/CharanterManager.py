##
# @file CharacterManager.py
# @version 20221214
# @author HikaruSatomura
import random
from .BattleDefine import *
from .Player import Player
from .Enemy import Enemy
from typing import List

##
# @class CharanterManager
# @brief キャラクターの管理を行うクラス
class CharacterManager:
    ##
    # @fn __init()
    # @brief 初期化
    # @return なし
    def __init__(self) -> None:
        self.__playerList : list = list()
        self.__enemyList : list = list()

    ##
    # @fn CreateCharacter(CharacterType)
    # @brief 指定した種類のキャラクターを作成する
    # @param [in] type CharacterType
    # @return なし
    def CreateCharacter(self, type : CharacterType):
        if type == CharacterType.Player:            
            createPos = self.CalcCaracterCreatePosition(
                CharacterPositonDefine.UnitXStart,
                CharacterPositonDefine.UnitXEnd,
                CharacterPositonDefine.PlayerYStart,
                CharacterPositonDefine.PlayerYEnd,
                self.PlayerList )

            id = random.randint(CharacterNum.PlayerStart, CharacterNum.PlayerMax)  # excelのプレイヤーの種類
                
            self.PlayerList.append(Player(createPos.X, createPos.Y, id, len(self.PlayerList)))
        elif type == CharacterType.Enemy:
            createPos = self.CalcCaracterCreatePosition(
                CharacterPositonDefine.UnitXStart,
                CharacterPositonDefine.UnitXEnd,
                CharacterPositonDefine.EnemyYStart,
                CharacterPositonDefine.EnemyYEnd,
                self.EnemyList )
            
            id = random.randint(CharacterNum.EnemyStart, CharacterNum.EnemyMax) # excelのエネミーの種類
                
            self.PlayerList.append(Enemy(createPos.X, createPos.Y, id, len(self.EnemyList)))
            
    ##
    # @fn CalcCharacterCreatePosition(int,int,int,int)
    # @brief キャラクターを生成する際の座標を計算する
    # @param [in] xStart 生成位置のX開始座標
    # @param [in] xEnd 生成位置のX終了座標
    # @param [in] yStart 生成位置のy開始座標
    # @param [in] yEnd 生成位置のy終了座標
    # @param [in] checkList 重複を確認するキャラクターのリスト
    # @return 生成する座標
    def CalcCaracterCreatePosition(self, xStart : int, xEnd : int, yStart : int, yEnd : int, characterList : list) -> BattleMapPos:
        result = BattleMapPos(0, 0)
        while True:
            x = random.randint(xStart, xEnd)
            y = random.randint(yStart, yEnd)

            # 既に生成されているキャラクターと被らないように確認
            isSearchEnd : bool = True
            for character in characterList:
                pos = character.MapPos
                if pos.X == x and pos.Y == y:
                    isSearchEnd = False
                    break

            if isSearchEnd:
                result.SetPos(x, y)
                break;

        return result

    @property
    def PlayerList(self):
        return self.__playerList
    @property
    def EnemyList(self):
        return self.__enemyList
        