import tkinter as tk
import sys, os
sys.path.append('../../Script/Display/')
from Script.Display.GameDraw import GameDraw

sys.path.append('../../Script/System/IO/')
from Script.System.IO.InputManager import InputManager

class Game:    
    def __init__(self, tkIntance):
        self.tkIntance = tkIntance
        self.gd = GameDraw(self.tkIntance)
        self.inputManager = InputManager(tkIntance)

