from tkinter import *
from PIL import Image, ImageTk
from pyautogui import moveTo
import time
import math as m

# создаём новый объект — окно с игровым полем.
tk = Tk()
tk.title('Game')

# запрещаем менять размеры окна, для этого используем свойство resizable
tk.resizable(0, 0)
# помещаем наше игровое окно выше остальных окон на компьютере, чтобы другие окна не могли его заслонить.
tk.wm_attributes('-topmost', 1)
tk.config(cursor='cross')
# Globals
WIDTH = 1200
HEIGHT = 800

# узнаем размеры экрана в пикселях
SCREEN_WIDTH = tk.winfo_screenwidth()
SCREEN_HEIGHT = tk.winfo_screenheight()

# создаём новый холст — 1200 на 800 пикселей и размещаем его по центру, где и будем рисовать игру
tk.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, int((SCREEN_WIDTH - WIDTH) / 2), int((SCREEN_HEIGHT - HEIGHT) / 2)))
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
# говорим холсту, что у каждого видимого элемента будут свои отдельные координаты
canvas.pack()
# обновляем окно с холстом
tk.update()


def win():
    pass


class CameraMotion(object):

    def __init__(self):
        moveTo(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.change_coord_x = 0
        self.change_coord_y = 0
        self.bind()

    def return_data(self):
        return self.change_coord_x, self.change_coord_y

    def motion(self, event):
        self.change_coord_x = WIDTH / 2 - event.x
        self.change_coord_y = HEIGHT / 2 - event.y
        moveTo(tk.winfo_rootx() + WIDTH / 2, tk.winfo_rooty() + HEIGHT / 2)
        canvas.delete(ALL)

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
        self.edge_ident = 0
        time.sleep(0.01)
        self.motion()

    def motion(self):
        self.coord_x += camera.return_data()[0]
        self.coord_y += camera.return_data()[1]
        canvas.delete(self.image_sprite)
        self.image_sprite = canvas.create_image(self.coord_x, self.coord_y, image=self.image, anchor="nw")
        time.sleep(0.01)
        canvas.after(20, self.motion)

    def return_size(self):
        return self.width, self.height


class Stickman(object):

    def __init__(self, way_to_stickman_sprites, way_to_customization_sprites):
        self.change_time = []
        self.sprites = []
        self.image_coord_list = []
        self.head_coord_list = []
        self.customization_sprites = way_to_customization_sprites
        self.head_angle = []
        self.head_r = []
        with open(way_to_stickman_sprites, "r") as file_data:
            self.all = file_data.read().split()
        for i in range(0, len(self.all), 8):
            self.sprites.append(self.all[i])
            self.change_time.append(self.all[i + 1])
            self.image_coord_list.append((int(self.all[i + 2]), int(self.all[i + 3])))
            self.head_coord_list.append((int(self.all[i + 4]), int(self.all[i + 5])))
            self.head_angle.append(int(self.all[i + 6]))
            self.head_r.append(int(self.all[i + 7]))
        self.offset_x = 0
        self.offset_y = 0
        self.number_of_sprites = int(len(self.all) / 8)
        self.start_ident = 1
        self.counter = 0
        self.clothes = Customization(self.number_of_sprites, self.head_coord_list, self.sprites,
                                     self.customization_sprites, self.head_angle)
        self.sprites = self.clothes.return_sprites()
        self.image = self.sprites[0]
        self.image_sprite = canvas.create_image(self.image_coord_list[0][0], self.image_coord_list[0][1],
                                                image=self.image, anchor="nw")
        self.motion()
        self.update()
        canvas.bind("<Button-1>", self.shoot)

    def animation(self):
        if self.counter == self.number_of_sprites:
            self.counter = 0
        self.image = self.sprites[self.counter]
        canvas.delete(self.image_sprite)
        self.image_sprite = canvas.create_image(self.image_coord_list[self.counter][0] + self.offset_x,
                                                self.image_coord_list[self.counter][1] + self.offset_y,
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
        self.image_sprite = canvas.create_image(self.image_coord_list[self.counter][0] + self.offset_x,
                                                self.image_coord_list[self.counter][1] + self.offset_y,
                                                image=self.image, anchor="nw")
        canvas.after(20, self.motion)

    def start(self):
        self.start_ident = 1
        self.update()

    def pause(self):
        self.start_ident = 0

    def shoot(self, event):
        if (self.head_coord_list[self.counter][0] + self.image_coord_list[self.counter][0] +
            self.offset_x - event.x)**2 + (self.head_coord_list[self.counter][1] +
                                           self.image_coord_list[self.counter][1] + self.offset_y - event.y)**2 \
                <= self.head_r[self.counter]**2:
            print(1)
            win()


class Customization(object):
    def __init__(self, number_of_sprites, head_coords_list, stickman_sprites, customization_sprites,
                 customization_sprites_angle):
        self.number_of_sprites = number_of_sprites
        self.head_coords_list = head_coords_list
        self.stickman_sprites = stickman_sprites
        self.cus_sprites = customization_sprites
        self.angle = customization_sprites_angle
        self.changed_sprites = list()
        for i in range(0, self.number_of_sprites):
            self.stickman_pil_im = Image.open(self.stickman_sprites[i])
            self.cus_pilImage = Image.open(self.cus_sprites)
            self.rotated_customization_image = self.cus_pilImage.rotate(self.angle[i])
            self.stickman_pil_im.paste(self.rotated_customization_image,
                                       [self.head_coords_list[i][0] - int(
                                           self.cus_pilImage.size[0] / 2 * m.cos(m.radians(self.angle[i])) +
                                           self.cus_pilImage.size[1] * m.sin(m.radians(self.angle[i]))),
                                        self.head_coords_list[i][1] - int(
                                            self.cus_pilImage.size[1] - self.cus_pilImage.size[0] / 2 * m.sin(
                                                m.radians(self.angle[i])))],
                                       self.rotated_customization_image)
            self.image = ImageTk.PhotoImage(self.stickman_pil_im)
            self.changed_sprites.append(self.image)

    def return_sprites(self):
        return self.changed_sprites


class Scope(object):
    def __init__(self, way_to_scope_sprite):
        self.pilImage_scope = Image.open(way_to_scope_sprite)
        self.scope_sprite = ImageTk.PhotoImage(self.pilImage_scope)
        self.scope_image = canvas.create_image(int((WIDTH - self.pilImage_scope.size[0]) / 2),
                                               int((HEIGHT - self.pilImage_scope.size[1]) / 2),
                                               image=self.scope_sprite, anchor="nw")
        self.update()

    def update(self):
        self.scope_image = canvas.create_image(int((WIDTH - self.pilImage_scope.size[0]) / 2),
                                               int((HEIGHT - self.pilImage_scope.size[1]) / 2),
                                               image=self.scope_sprite, anchor="nw")
        canvas.after(100, self.update)


camera = CameraMotion()
map = MapCanvas("Images/Maps/Game.jpg")
st_1 = Stickman("Images/Stickmen/Stickman_exercise/Stickman_exercise.txt", "Images/Customization resources/Hat-1.png")
time.sleep(0.01)
tk.focus_set()
tk.mainloop()
