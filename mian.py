import pygame

import sys, os
sys.path.append('/Script/Data/')
from Script.Data.GameData import GameData
sys.path.append('/Script/Display/')
from Script.Display.Game import Game

gd = GameData()
gd.LoadData()

game = Game()

print(gd.GetCharacterDataFromId(1).characterName)
print(gd.GetWeaponDataFromId(1).weaponName)


from pygame.locals import *
# ゲーム画面を初期化
pygame.init()
screen = pygame.display.set_mode((600, 400))
white = (255,255,255)
black = (0,0,0)

# ゲームループ
while True:
    screen.fill(black) # 背景を黒で塗りつぶす

    game.Update()
    game.Draw()
    
    # 画面を更新
    pygame.display.update()
    # 終了イベントを確認 --- (*5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

