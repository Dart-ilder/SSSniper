from tkinter import *
from PIL import Image, ImageTk
import time
import random

tk = Tk()
tk.title('Game')
tk.config(cursor='plus')

tk.resizable(0, 0)

tk.wm_attributes('-topmost', 1)

WIDTH = 1200
HEIGHT = 800

canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
tk.update()


class Menu():
    def __init__(self, canvas, status):
        self.canvas = canvas

        self.NAMEPic = ('Stickmen/SSSniper.png', 620, 80)
        self.START_B = ('Stickmen/start_b.png', 600, 200)
        self.START_S = ('Stickmen/start_s.png', 600, 200)
        self.SETTINGS_B = ('Stickmen/settings_b.png', 600, 300)
        self.SETTINGS_S = ('Stickmen/settings_s.png', 600, 300)
        self.CHOOSE_B = ('Stickmen/choose_b.png', 600, 440)
        self.CHOOSE_S = ('Stickmen/choose_s.png', 600, 440)

        self.NAMEload = ImageTk.PhotoImage(Image.open(self.NAMEPic[0]))
        self.CHOOSE_S_load = ImageTk.PhotoImage(Image.open(self.CHOOSE_S[0]))
        self.CHOOSE_B_load = ImageTk.PhotoImage(Image.open(self.CHOOSE_B[0]))
        self.SETTINGS_S_load = ImageTk.PhotoImage(Image.open(self.SETTINGS_S[0]))
        self.SETTINGS_B_load = ImageTk.PhotoImage(Image.open(self.SETTINGS_B[0]))
        self.START_S_load = ImageTk.PhotoImage(Image.open(self.START_S[0]))
        self.START_B_load = ImageTk.PhotoImage(Image.open(self.START_B[0]))

        if status == 'menu':
            self.START = canvas.create_image(self.START_S[1], self.START_S[2], image=self.START_S_load)
            self.NAME = canvas.create_image(self.NAMEPic[1], self.NAMEPic[2], image=self.NAMEload)
            self.SETTINGS = canvas.create_image(self.SETTINGS_S[1], self.SETTINGS_S[2], image=self.SETTINGS_S_load)
            self.CHOOSE = canvas.create_image(self.CHOOSE_S[1], self.CHOOSE_S[2], image=self.CHOOSE_S_load)

    def inside(obj, obj_s_load, x, y, canvas):
        if canvas.coords(obj)[0] - obj_s_load.width() * 0.5 < x < canvas.coords(obj)[
            0] + obj_s_load.width() * 0.5 and canvas.coords(obj)[
            1] - obj_s_load.height() * 0.5 < y < canvas.coords(obj)[
            1] + obj_s_load.height() * 0.5:
            return True
        else:
            return False

    def PICchange(obj, obj_s_load, x, y, canvas, obj_b_load, obj_s, obj_b):
        if Menu.inside(obj, obj_s_load, x, y, canvas):
            canvas.delete(obj)
            obj = canvas.create_image(obj_b[1], obj_b[2], image=obj_b_load)
        else:
            canvas.delete(obj)
            obj = canvas.create_image(obj_s[1], obj_s[2], image=obj_s_load)
        return obj

    def motion(self, event):
        x, y = event.x, event.y
        self.START = Menu.PICchange(self.START, self.START_S_load, x, y, canvas, self.START_B_load, self.START_S,
                                    self.START_B)
        self.SETTINGS = Menu.PICchange(self.SETTINGS, self.SETTINGS_S_load, x, y, canvas, self.SETTINGS_B_load,
                                       self.SETTINGS_S, self.SETTINGS_B)
        self.CHOOSE = Menu.PICchange(self.CHOOSE, self.CHOOSE_S_load, x, y, canvas, self.CHOOSE_B_load, self.CHOOSE_S,
                                     self.CHOOSE_B)

    def go_to(self, event):
        x, y = event.x, event.y
        if Menu.inside(self.START, self.START_S_load, x, y, self.canvas):
            self.canvas.delete('all')
            tk.bind('<Button-1>', '')
            tk.bind('<Motion>', '')
            print('lets play')
        elif Menu.inside(self.SETTINGS, self.SETTINGS_S_load, x, y, self.canvas):
            self.canvas.delete('all')
            settings = Menu(self.canvas, 'settings')
            tk.bind('<Button-1>', '')
            tk.bind('<Motion>', '')
        elif Menu.inside(self.CHOOSE, self.CHOOSE_S_load, x, y, self.canvas):
            self.canvas.delete('all')
            choose = Menu(self.canvas, 'choose')
            tk.bind('<Button-1>', '')
            tk.bind('<Motion>', '')

menu = Menu(canvas, 'menu')
tk.bind('<Motion>', menu.motion)
tk.bind('<Button-1>', menu.go_to)

tk.mainloop()
