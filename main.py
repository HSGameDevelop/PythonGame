import sys, os
sys.path.append('/Script/Display/')
from Script.Game import Game

game = Game()

# ゲームループ
while not game.CheckEnd():
    game.Update()
    game.Draw()

sys.exit()
