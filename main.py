import sys, os
sys.path.append('/Script/Data/')
from Script.Data.GameData import GameData
sys.path.append('/Script/Display/')
from Script.Game import Game

gd = GameData()
gd.LoadData()

game = Game()

print(gd.GetCharacterDataFromId(1).characterName)
print(gd.GetWeaponDataFromId(1).weaponName)


# ゲームループ
while not game.CheckEnd():
    game.Update()
    game.Draw()

sys.exit()
