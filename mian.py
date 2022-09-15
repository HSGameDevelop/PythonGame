import tkinter as tk
import sys, os
sys.path.append('/Script/Data/')
from Script.Data.GameData import GameData
sys.path.append('/Script/Display/')
from Script.Display.Game import Game

gd = GameData()
gd.LoadData()

print(gd.GetCharacterDataFromId(1).characterName)
print(gd.GetWeaponDataFromId(1).weaponName)

app = tk.Tk()
app.geometry("1280x960")
app.title('Kings')
game = Game(app)
app.mainloop()