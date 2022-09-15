import sys, os
sys.path.append('/Script/Data/')
from Script.Data.GameData import GameData

gd = GameData()
gd.LoadData()

a = 'Hello'
b = 'World'
print (a + b)