import tkinter as tk
import Hexagon as Hexa

app = tk.Tk()
app.geometry("1280x960")
app.title('player test')
Hex = Hexa.Hexagon(app)

class Player:
    def __init__(self, master):
        '''コンストラクタ'''

        self.master = master    #   親ウィジェット
        self.board = None       #   盤面上のユニットを管理する2次元リスト
        self.h_w = 45
        self.h_w1_4 = 45 / 4
        self.h_w1_2 = 45 / 2
        self.h_w3_4 = 45 * (3 / 4)

        # ウィジェットの作成
        self.createWidgets()

        # ゲームの初期化
        #self.initPlayer()
    
    def createWidgets(self):
        '''ウィジェットを作成・配置する'''




app.mainloop()
