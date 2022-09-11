import tkinter as tk
# マップ表示のクラス
import Hexagon as Hexa
# プレイヤー表示のクラス　未完
#import Player

class Game:
    
    def __init__(self, master):
        self.master = master
        
        # Mapの表示
        self.screen = Hexa.Hexagon(self.master)



app = tk.Tk()
app.geometry("1280x960")
app.title('world trigger')
game = Game(app)
#class2 = Player.Player(app)
app.mainloop()
