# 移動時のマップのマスの範囲とかの計算クラス
second = 2


class MoveMethod():
    # 初期化
    def __init__(self) -> None:
        pass

    # マップのマスの範囲（移動・視野）を求める
    def DistanceReverse(x, y, distance):
        area = []
        distance_ex = distance + 1
        for col in range(distance_ex):
            for row in range(distance_ex + col):
                if (y - distance + col) % 2 == 0:
                    area.append([ ((x - distance) + ((row - col) * second)) / 2, (y - distance) + col])
                #elif (y - distance + col) % 2 == 1:
                #    area.append([ ((x - distance) + ((row - col) * second)) / 2, (y - distance) + col])
        
        #for col in range(distance):
        #    for row in range( (distance * second) - col):
                #if ((y + 1) + col) % 2 == 0:
                #    area.append([ ((x - (distance * second) + 1) + ((row + col) * second)) / 2, (y + 1) + col])
                #elif ((y + 1) + col) % 2 == 1:
                #    area.append([ ((x - (distance * second) + 1) + ((row + col) * second)) / 2 - 1, (y + 1) + col])
        return area

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
        
