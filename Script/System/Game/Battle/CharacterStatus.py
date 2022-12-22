from ..Data.GameData import CharacterData

class CharacterStatus:
    def __init__(self, data : CharacterData) -> None:
        self.__characterId       = data.characterId             # キャラクターID
        self.__characterName     = data.characterName           # キャラクター名
        self.__actionPower       = int(data.actionpower)        # 行動力
        self.__hitPoint          = int(data.hitpoint)           # HP
        self.__attackPoint       = int(data.attackpoint)        # 攻撃力
        self.__deffencePoint     = int(data.defensepoint)       # 防御力
        self.__avoidancePoint    = int(data.avoidancepoint)     # 回避力
        self.__technologyPoint   = int(data.technologypoint)    # 技術力
        self.__visible           = int(data.visible)            # 視界

    @property
    def CharacterId(self) -> int:
        return self.__characterId
    @CharacterId.setter
    def CharacterId(self, id) -> None:
        self.__characterId = id

    @property
    def CharacterName(self) -> int:
        return self.__characterName
    @CharacterName.setter
    def characterName(self, name) -> None:
        self.__characterName = name

    @property
    def ActionPower(self) -> int:
        return self.__actionPower
    @ActionPower.setter
    def ActionPower(self, actionPower) -> None:
        self.__ActionPower = actionPower

    @property
    def HitPoint(self) -> int:
        return self.__hitPoint
    @HitPoint.setter
    def HitPoint(self, hitPoint) -> None:
        self.__hitPoint = hitPoint

    @property
    def AttackPoint(self) -> int:
        return self.__attackPoint
    @AttackPoint.setter
    def AttackPoint(self, attackPoint) -> None:
        self.__attackPoint = attackPoint

    @property
    def DeffencePoint(self) -> int:
        return self.__deffencePoint
    @DeffencePoint.setter
    def DeffencePoint(self, defencePoint) -> None:
        self.__deffencePoint = defencePoint

    @property
    def AvoidancePoint(self) -> int:
        return self.__avoidancePoint
    @AvoidancePoint.setter
    def AvoidancePoint(self, avoidancePoint) -> None:
        self.__avoidancePoint = avoidancePoint

    @property
    def TechnologyPoint(self) -> int:
        return self.__technologyPoint
    @TechnologyPoint.setter
    def TechnologyPoint(self, technologyPoint) -> None:
        self.__technologyPoint = technologyPoint

    @property
    def Visible(self) -> int:
        return self.__visible
    @Visible.setter
    def Visible(self, visible) -> None:
        self.__visible = visible
