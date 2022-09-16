import tkinter

import sys, os
sys.path.append('../../Script/System/IO/')
from Script.System.IO.InputKeyboard import InputKeyboard

class InputManager:
    def __init__(self, tkInstance : tkinter) -> None:
        self.intputKeyboard = InputKeyboard(tkInstance)
