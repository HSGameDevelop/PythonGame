import tkinter as tk
# マップ表示のクラス
import Hexagon as Hexa
# プレイヤー表示のクラス　未完
import Player

class Game:
    
    def __init__(self, master):
        self.master = master
        
        # Mapの表示
        self.screen = Hexa.Hexagon(self.master)

        # ↓これを追加
        self.characters = []
        self.player = Player.Player(self.master)

        #self.update()

        #player_infos = []
        #for character in self.characters:
        #    player = character.getPlayer()
        #    player_infos.append(player)
        
        #self.screen.update(player_infos)
        
        #self.screen.update(image_infos)



app = tk.Tk()
app.geometry("1280x960")
app.title('world trigger')
game = Game(app)
#player = Player.Player(app)
app.mainloop()
