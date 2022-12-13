from enum import Enum, IntEnum

class SideType(Enum):
    Player = 0,
    Enemy = 1

class CharacterNum(IntEnum):
    PlayerStart = 1,
    PlayerMax = 25,
    EnemyStart = 26,
    EnemyMax = 50
