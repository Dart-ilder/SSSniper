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
CAMERA_V_X = 4
CAMERA_V_Y = 2

# создаём новый холст — 1200 на 800 пикселей, где и будем рисовать игру
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
# говорим холсту, что у каждого видимого элемента будут свои отдельные координаты
canvas.pack()
# обновляем окно с холстом
tk.update()


class CameraMotion():

    def __init__(self):
        self.change_coord_x = 0
        self.change_coord_y = 0
        self.bind()
        self.update_time()

    def return_data(self):
        return self.change_coord_x, self.change_coord_y

    def motion(self, event):
        if (WIDTH * 5 / 6 > event.x > WIDTH / 6 and HEIGHT * 4 / 5 > event.y > HEIGHT / 5) is False:
            if event.x < WIDTH / 6:
                if event.y < HEIGHT / 2:
                    self.change_coord_x = CAMERA_V_X / (WIDTH / 6) * (WIDTH / 6 - event.x)
                    self.change_coord_y = CAMERA_V_Y / (HEIGHT / 2) * (HEIGHT / 2 - event.y) * 2 / 5
                elif event.y > HEIGHT / 2:
                    self.change_coord_x = CAMERA_V_X / (WIDTH / 6) * (WIDTH / 6 - event.x)
                    self.change_coord_y = -CAMERA_V_Y / (HEIGHT / 2) * (event.y - HEIGHT / 2) * 2 / 5
            elif event.x > WIDTH * 5 / 6:
                if event.y < HEIGHT / 2:
                    self.change_coord_x = -CAMERA_V_X / (WIDTH / 6) * (event.x - WIDTH * 5 / 6)
                    self.change_coord_y = CAMERA_V_Y / (HEIGHT / 2) * (HEIGHT / 2 - event.y) * 2 / 5
                elif event.y > HEIGHT / 2:
                    self.change_coord_x = -CAMERA_V_X / (WIDTH / 6) * (event.x - WIDTH * 5 / 6)
                    self.change_coord_y = -CAMERA_V_Y / (HEIGHT / 2) * (event.y - HEIGHT / 2) * 2 / 5
            elif event.y < HEIGHT / 5:
                if event.x < WIDTH / 2:
                    self.change_coord_x = CAMERA_V_X / (WIDTH / 2) * (WIDTH / 2 - event.x) / 6
                    self.change_coord_y = CAMERA_V_Y / (HEIGHT / 5) * (HEIGHT / 5 - event.y)
                elif event.x > WIDTH / 2:
                    self.change_coord_x = -CAMERA_V_X / (WIDTH / 2) * (event.x - WIDTH / 2) / 6
                    self.change_coord_y = CAMERA_V_Y / (HEIGHT / 5) * (HEIGHT / 5 - event.y)
            elif event.y > HEIGHT * 4 / 5:
                if event.x < WIDTH / 2:
                    self.change_coord_x = CAMERA_V_X / (WIDTH / 2) * (WIDTH / 2 - event.x) / 6
                    self.change_coord_y = -CAMERA_V_Y / (HEIGHT / 5) * (event.y - HEIGHT * 4 / 5)
                elif event.x > WIDTH / 2:
                    self.change_coord_x = -CAMERA_V_X / (WIDTH / 2) * (event.x - WIDTH / 2) / 6
                    self.change_coord_y = -CAMERA_V_Y / (HEIGHT / 5) * (event.y - HEIGHT * 4 / 5)
        else:
            self.change_coord_x = 0
            self.change_coord_y = 0

    def update_time(self):
        time.sleep(0.01)
        canvas.after(20, self.update_time)

    def bind(self):
        canvas.bind("<Motion>", self.motion)


class MapCanvas(object):

    def __init__(self, file_name):
        self.pilImage = Image.open(file_name)
        self.width = self.pilImage.size[0]
        self.height = self.pilImage.size[1]
        self.image = ImageTk.PhotoImage(self.pilImage)
        self.coord_x = (-self.width + WIDTH) / 2
        self.coord_y = (-self.height + HEIGHT) / 2
        self.image_sprite = canvas.create_image(self.coord_x, self.coord_y, image=self.image, anchor="nw")
        self.motion()

    def motion(self):
        self.coord_x += camera.return_data()[0]
        self.coord_y += camera.return_data()[1]
        canvas.delete(self.image_sprite)
        self.image_sprite = canvas.create_image(self.coord_x, self.coord_y, image=self.image, anchor="nw")
        canvas.after(20, self.motion)


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
            self.coord_x.append(int(self.all[i+2]))
            self.coord_y.append(int(self.all[i+3]))
        self.offset_x = 0
        self.offset_y = 0
        self.number_of_sprites = int(len(self.all)/4)
        self.start_ident = 1
        self.counter = 0
        self.pilImage = Image.open(self.sprites[0])
        self.image = ImageTk.PhotoImage(self.pilImage)
        self.image_sprite = canvas.create_image(self.coord_x[0], self.coord_y[0], image=self.image, anchor="nw")
        self.motion()
        self.update()

    def animation(self):
        if self.counter == self.number_of_sprites:
            self.counter = 0
        self.pilImage = Image.open(self.sprites[self.counter])
        self.image = ImageTk.PhotoImage(self.pilImage)
        canvas.delete(self.image_sprite)
        self.image_sprite = canvas.create_image(self.coord_x[self.counter] + self.offset_x,
                                                self.coord_y[self.counter] + self.offset_y,
                                                image=self.image, anchor="nw")

    def update(self):
        if self.start_ident:
            self.counter += 1
            self.animation()
            canvas.after(self.change_time[self.counter], self.update)

    def motion(self):
        self.offset_x += camera.return_data()[0]
        self.offset_y += camera.return_data()[1]
        canvas.delete(self.image_sprite)
        self.image_sprite = canvas.create_image(self.coord_x[self.counter] + self.offset_x,
                                                self.coord_y[self.counter] + self.offset_y,
                                                image=self.image, anchor="nw")
        canvas.after(20, self.motion)

    def start(self):
        self.start_ident = 1
        self.update()

    def pause(self):
        self.start_ident = 0


camera = CameraMotion()
x = MapCanvas("Maps\Game.jpg")
z = Stickman("Stickmen\Stickman_exercise\Stickman_exercise.txt")
tk.mainloop()
