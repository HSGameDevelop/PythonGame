import numpy as np

class GameDefine:
    # 座標
    class Position:
        def __init__(self, x : float = 0, y : float = 0) -> None:
            self.x = x
            self.y = y

    # サイズ
    class Size:
        def __init__(self, width : float = 0, height : float = 0) -> None:
            self.width = width
            self.height = height

    # 向き
    class Direction:
        def __init__(self, x : float = 0, y : float = 0) -> None:
            self.x = x
            self.y = y
            
    DEFAULT_DIRECTION = np.array([1, 0])
    DEFAULT_DISTANCE = np.linalg.norm(DEFAULT_DIRECTION)
