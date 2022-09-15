import tkinter as tk
import sys, os
sys.path.append('../../Script/Display/')
from Script.Display.GameDraw import GameDraw

class Game:    
    def __init__(self, master):
        self.master = master
        self.gd = GameDraw(self.master)

