from tkinter import *
from PIL import Image, ImageTk
import time
import random

# создаём новый объект — окно с игровым полем.
tk = Tk()
tk.title('Game')
# запрещаем менять размеры окна, для этого используем свойство resizable
tk.resizable(0, 0)
# помещаем наше игровое окно выше остальных окон на компьютере, чтобы другие окна не могли его заслонить.
tk.wm_attributes('-topmost', 1)

# Globals
WIDTH = 1200
HEIGHT = 800

# создаём новый холст — 1200 на 800 пикселей, где и будем рисовать игру
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
# говорим холсту, что у каждого видимого элемента будут свои отдельные координаты
canvas.pack()
# обновляем окно с холстом
tk.update()


class MapCanvas(object):

    def __init__(self, file_name):
        self.pilImage = Image.open(file_name)
        self.width = self.pilImage.size[0]
        self.height = self.pilImage.size[1]
        self.image = ImageTk.PhotoImage(self.pilImage)
        self.imagesprite = canvas.create_image((-self.width + WIDTH) / 2, (-self.height + HEIGHT) / 2,
                                               image=self.image, anchor="nw")
        print(file_name)


class Stickman(object):

    def __init__(self, way_to_sprites):
        self.change_time = []
        self.sprites = []
        self.coord_x = []
        self.coord_y = []
        with open(way_to_sprites, "r") as file_data:
            self.all = file_data.read().split()
        for i in range(0, len(self.all), 4):
            self.sprites.append(self.all[i])
            self.change_time.append(self.all[i+1])
            self.coord_x.append(self.all[i+2])
            self.coord_y.append(self.all[i+3])
        self.number_of_sprites = int(len(self.all)/4)
        self.start_ident = 1
        self.counter = 0
        self.pilImage = Image.open(self.sprites[0])
        self.image = ImageTk.PhotoImage(self.pilImage)
        self.imagesprite = canvas.create_image(self.coord_x[0], self.coord_y[0], image=self.image, anchor="nw")
        self.update()

    def animation(self):
        if self.counter == self.number_of_sprites:
            self.counter = 0
        self.pilImage = Image.open(self.sprites[self.counter])
        self.width = self.pilImage.size[0]
        self.height = self.pilImage.size[1]
        self.image = ImageTk.PhotoImage(self.pilImage)
        self.imagesprite = canvas.create_image(self.coord_x[self.counter], self.coord_y[self.counter],
                                               image=self.image, anchor="nw")
        canvas.after(self.change_time[self.counter], self.update)

    def start(self):
        self.start_ident = 1
        self.update()

    def pause(self):
        self.start_ident = 0

    def update(self):
        if self.start_ident:
            self.counter += 1
            self.animation()


x = MapCanvas("Maps\Game.jpg")
z = Stickman("Stickmen\Stickman_exercise\Stickman_exercise.txt")
tk.mainloop()
