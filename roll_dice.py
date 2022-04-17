from random import seed
from random import randint
from pygame_lib import *
from tkinter import *


class dice_roll:
    def __init__(self):
        self.range_min = 0
        self.range_max = 6
        self.possibilities = [1, 2, 3, 4, 5, 6]
        self.dice_roll = random_roll()

    def random_roll(self):
        seed(1)
        self.value = randint(self.range_min, self.range_max)
        self.roll = possibilities[self.value]


class gfx:
    def __init__(self):
        self.face_1 = makeSprite("/d_faces/1.png")
        self.face_2 = makeSprite("/d_faces/2.png")
        self.face_3 = makeSprite("/d_faces/3.png")
        self.face_4 = makeSprite("/d_faces/4.png")
        self.face_5 = makeSprite("/d_faces/5.png")
        self.face_6 = makeSprite("/d_faces/6.png")
        self.dice_width = res_width()
        self.dice_height = res_height()

        screenSize(res_width() / 2, res_height() / 2, res_width() / 2, res_height() / 2)
        setIcon("/d_faces/favicon.png")
        setWindowTitle("Dice Roll by Rohaan")

    def res_width(self):
        root = Tkinter.Tk()
        self.width = root.winfo_screenwidth()
        return self.res_width

    def res_hight(self):
        root = Tkinter.Tk()
        self.height = root.winfo_screenheight()
        return self.res_hight

    def show1(self):
        showSprite(self.face_1)
        moveSprite(self.face_1, res_width(), res_height())

    def show2(self):
        showSprite(self.face_2)
        moveSprite(self.face_2, res_width(), res_height())

    def show3(self):
        showSprite(self.face_3)
        moveSprite(self.face_3, res_width(), res_height())

    def show4(self):
        showSprite(self.face_4)
        moveSprite(self.face_4, res_width(), res_height())

    def show5(self):
        showSprite(self.face_5)
        moveSprite(self.face_5, res_width(), res_height())

    def show6(self):
        showSprite(self.face_6)
        moveSprite(self.face_6, res_width(), res_height())
