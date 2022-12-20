# 移動時のマップのマスの範囲とかの計算クラス
second = 2


class MoveMethod():
    # 初期化
    def __init__(self) -> None:
        pass

    # マップのマスの範囲（移動・視野）を求める
    def distance_reverse(x, y, distance):
        # 東
        east = [(distance * second + x), y]
        # 西
        west = [(x - distance * second), y]
        for col in range(distance * second + 1):
            if col == 0 or col == distance * second + 1:
                for raw in range(distance * second + 1):
                    north_east = [(x + distance), y  - distance]
                    # north_west = [ x - distance, y]
                    # distance * 2 から distance + 1 まで
                    # for num in range(distance + 1, distance * 2 + 1):
            elif col == 1 or col == distance * second:
                for raw in range(distance * second):
                    north_east = [(x + distance), y  - distance]
            elif col == 2 or col == distance * second - 1:
                for raw in range(distance * second - 1):
                    north_east = [(x + distance), y  - distance]

            # 南西
            south_west = [(x - distance), y + distance]
            # 南東
            south_east = [(x + distance), y + distance]
            # この六角形をどう繋げるか
        pass    

    # マップのマスの範囲（移動・視野）を求める
    def double_distance(player_x, player_y, x, y):
        pass

    def doublewidth_distance(a, b):
        dcol = abs(a.col - b.col)
        drow = abs(a.row - b.row)
        return drow + max( 0, (dcol - drow) / 2)

    def doubleheight_distance(a, b):
        dcol = abs(a.col - b.col)
        drow = abs(a.row - b.row)
        return dcol + max( 0, (drow - dcol) / 2)
        
