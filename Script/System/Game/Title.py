import sys
from .GameSequenceBase import GameSequenceBase
from .PgLib import PgLib
import pygame



class Title(GameSequenceBase):
    def __init__(self, pgLib : PgLib) -> None:
        #画像の読み込み
        self.bgImage = pygame.image.load("Resource/Image/test_bg.jpg")
        self.pgLib = pgLib

    def Update(self):
        pass

    def Draw(self):
        screen = self.pgLib.GetScreen()

        screen.blit(self.bgImage, (0, 0, 1280, 960))