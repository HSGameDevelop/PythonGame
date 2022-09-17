import sys, os
sys.path.append('/Script/Data/')
from Script.Data.GameData import GameData
sys.path.append('/Script/Display/')
from Script.System.Game.Game import Game

gd = GameData()
gd.LoadData()

game = Game()

print(gd.GetCharacterDataFromId(1).characterName)
print(gd.GetWeaponDataFromId(1).weaponName)


# ゲームループ
while True:
    game.Update()
    game.Draw()
    
    if game.CheckEnd():
        sys.exit()

