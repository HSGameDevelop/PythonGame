import tkinter as tk
import GameDraw as GD

class Game:    
    def __init__(self, master):
        self.master = master

        self.gd = GD.GameDraw(self.master)


app = tk.Tk()
app.geometry("1280x960")
app.title('world trigger')
game = Game(app)
#player = Player.Player(app)
app.mainloop()
