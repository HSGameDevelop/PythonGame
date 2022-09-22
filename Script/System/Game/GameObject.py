import pygame.surface

# ゲームに使用するオブジェクトのクラス
class GameObject:
##########################
# パラメータ用クラス
# ########################    
    # 座標
    class Position:
        def __init__(self) -> None:
            self.x = 0
            self.y = 0

    # サイズ
    class Size:
        def __init__(self) -> None:
            self.width = 0
            self.height = 0

    # 向き
    class Direction:
        def __init__(self) -> None:
            self.x = 0
            self.y = 0

##########################
# メソッド
# ########################
    # 初期化
    def __init__(self) -> None:
        self.position = GameObject.Position()
        self.size = GameObject.Size()
        self.direction = GameObject.Direction()
        self.image : pygame.surface = None

    # 座標の取得
    def GetPos(self) -> Position:
        return self.position

    # 座標の設定
    def SetPos(self, x : int, y : int):
        self.position.x = x
        self.position.y = y

    # サイズの取得
    def GetSize(self) -> Size:
        return self.size

    # サイズの設定
    def SetSize(self, width : int, height: int):
        self.size.width = width
        self.size.height = height

    # 向きの取得
    def GetDir(self) -> Direction:
        return self.direction
    
    # 向きの設定
    def SetDir(self, x, y):
        self.direction.x = x
        self.direction.y = y

    # 画像の取得
    def GetImage(self) -> pygame.surface:
        return self.image

    # 画像の設定
    def SetImage(self, image : pygame.surface):
        self.image = image
    