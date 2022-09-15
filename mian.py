import sys, os
sys.path.append('/Script/Data/')
from Script.Data.GameData import GameData

gd = GameData()
gd.LoadData()

print(gd.GetCharacterDataFromId(1).characterName)
print(gd.GetWeaponDataFromId(1).weaponName)

a = 'Hello'
b = 'World'
print (a + b)