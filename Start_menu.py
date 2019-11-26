from tkinter import *
from PIL import Image, ImageTk
import sys

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


tk = Tk()
tk.title('Game')
tk.config(cursor='plus')
tk.configure(background=_from_rgb((235, 235, 235)))
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
        self.START_B = ('Stickmen/start_b.png', 600, 300)
        self.START_S = ('Stickmen/start_s.png', 600, 300)
        self.SETTINGS_B = ('Stickmen/settings_b.png', 601, 400)
        self.SETTINGS_S = ('Stickmen/settings_s.png', 601, 400)
        self.CHOOSE_B = ('Stickmen/choose_b.png', 600, 540)
        self.CHOOSE_S = ('Stickmen/choose_s.png', 600, 540)
        self.ABOUT_B = ('Stickmen/about_b.png', 597, 490)
        self.ABOUT_S = ('Stickmen/about_s.png', 597, 490)
        self.HOLEPic = ('Stickmen/hole.png', -50, 700)
        self.NEXT_S = ('Stickmen/next_s.png', 820, 330)
        self.NEXT_B = ('Stickmen/next_b.png', 820, 330)
        self.PREV_S = ('Stickmen/prev_s.png', 380, 330)
        self.PREV_B = ('Stickmen/prev_b.png', 380, 330)
        self.BACK_B = ('Stickmen/back_b.png', 30, 60)
        self.BACK_S = ('Stickmen/back_s.png', 30, 60)
        self.EXIT_S = ('Stickmen/exit_s.png', 600, 600)
        self.EXIT_B = ('Stickmen/exit_b.png', 600, 600)


        self.NAMEload = ImageTk.PhotoImage(Image.open(self.NAMEPic[0]))
        self.CHOOSE_S_load = ImageTk.PhotoImage(Image.open(self.CHOOSE_S[0]))
        self.CHOOSE_B_load = ImageTk.PhotoImage(Image.open(self.CHOOSE_B[0]))
        self.SETTINGS_S_load = ImageTk.PhotoImage(Image.open(self.SETTINGS_S[0]))
        self.SETTINGS_B_load = ImageTk.PhotoImage(Image.open(self.SETTINGS_B[0]))
        self.START_S_load = ImageTk.PhotoImage(Image.open(self.START_S[0]))
        self.START_B_load = ImageTk.PhotoImage(Image.open(self.START_B[0]))
        self.ABOUT_B_load = ImageTk.PhotoImage(Image.open(self.ABOUT_B[0]))
        self.ABOUT_S_load = ImageTk.PhotoImage(Image.open(self.ABOUT_S[0]))
        self.HOLEload = ImageTk.PhotoImage(Image.open(self.HOLEPic[0]))
        self.NEXT_B_load = ImageTk.PhotoImage(Image.open(self.NEXT_B[0]))
        self.NEXT_S_load = ImageTk.PhotoImage(Image.open(self.NEXT_S[0]))
        self.PREV_B_load = ImageTk.PhotoImage(Image.open(self.PREV_B[0]))
        self.PREV_S_load = ImageTk.PhotoImage(Image.open(self.PREV_S[0]))
        self.BACK_B_load = ImageTk.PhotoImage(Image.open(self.BACK_B[0]))
        self.BACK_S_load = ImageTk.PhotoImage(Image.open(self.BACK_S[0]))
        self.EXIT_S_load = ImageTk.PhotoImage(Image.open(self.EXIT_S[0]))
        self.EXIT_B_load = ImageTk.PhotoImage(Image.open(self.EXIT_B[0]))

        self.NAME = canvas.create_image(self.NAMEPic[1], self.NAMEPic[2], image=self.NAMEload)
        self.START = canvas.create_image(self.START_S[1], self.START_S[2], image=self.START_S_load)
        self.SETTINGS = canvas.create_image(self.SETTINGS_S[1], self.SETTINGS_S[2], image=self.SETTINGS_S_load)
        self.ABOUT = canvas.create_image(self.ABOUT_S[1], self.ABOUT_S[2], image=self.ABOUT_S_load)
        self.EXIT = canvas.create_image(self.EXIT_S[1], self.EXIT_S[2], image=self.EXIT_S_load)
        canvas.update()

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

    def motion_menu(self, event):
        x, y = event.x, event.y
        self.START = Menu.PICchange(self.START, self.START_S_load, x, y, canvas, self.START_B_load, self.START_S,
                                    self.START_B)
        self.SETTINGS = Menu.PICchange(self.SETTINGS, self.SETTINGS_S_load, x, y, canvas, self.SETTINGS_B_load,
                                       self.SETTINGS_S, self.SETTINGS_B)
        self.ABOUT = Menu.PICchange(self.ABOUT, self.ABOUT_S_load, x, y, canvas, self.ABOUT_B_load, self.ABOUT_S,
                                    self.ABOUT_B)
        self.EXIT = Menu.PICchange(self.EXIT, self.EXIT_S_load, x, y, canvas, self.EXIT_B_load, self.EXIT_S,
                                    self.EXIT_B)

    def motion_start(self, event):
        x, y = event.x, event.y
        self.CHOOSE = Menu.PICchange(self.CHOOSE, self.CHOOSE_S_load, x, y, canvas, self.CHOOSE_B_load, self.CHOOSE_S,
                                     self.CHOOSE_B)
        self.NEXT = Menu.PICchange(self.NEXT, self.NEXT_S_load, x, y, canvas, self.NEXT_B_load, self.NEXT_S,
                                   self.NEXT_B)
        self.PREV = Menu.PICchange(self.PREV, self.PREV_S_load, x, y, canvas, self.PREV_B_load, self.PREV_S,
                                   self.PREV_B)
        self.BACK = Menu.PICchange(self.BACK, self.BACK_S_load, x, y, canvas, self.BACK_B_load, self.BACK_S,
                                   self.BACK_B)

    def motion_settings(self, event):
        x, y = event.x, event.y
        self.BACK = Menu.PICchange(self.BACK, self.BACK_S_load, x, y, canvas, self.BACK_B_load, self.BACK_S,
                                   self.BACK_B)

    def go_to_menu(self, event):
        x, y = event.x, event.y
        if Menu.inside(self.START, self.START_S_load, x, y, self.canvas):
            self.canvas.delete(self.SETTINGS, self.ABOUT, self.START, self.EXIT)
            self.HOLE = canvas.create_image(self.HOLEPic[1], self.HOLEPic[2], image=self.HOLEload)
            self.CHOOSE = canvas.create_image(self.CHOOSE_S[1], self.CHOOSE_S[2], image=self.CHOOSE_S_load)
            self.NEXT = canvas.create_image(self.NEXT_S[1], self.NEXT_S[2], image=self.NEXT_S_load)
            self.PREV = canvas.create_image(self.PREV_S[1], self.PREV_S[2], image=self.PREV_S_load)
            self.BACK = canvas.create_image(self.BACK_S[1], self.BACK_S[2], image=self.BACK_S_load)
            tk.bind('<Motion>', menu.motion_start)
            tk.bind('<Button-1>', menu.go_back)
            tk.mainloop()
        elif Menu.inside(self.SETTINGS, self.SETTINGS_S_load, x, y, self.canvas):
            self.canvas.delete('all')
            self.BACK = canvas.create_image(self.BACK_S[1], self.BACK_S[2], image=self.BACK_S_load)
            self.NAME = canvas.create_image(self.NAMEPic[1], self.NAMEPic[2], image=self.NAMEload)
            tk.bind('<Button-1>', menu.go_back)
            tk.bind('<Motion>', menu.motion_settings)
        elif Menu.inside(self.ABOUT, self.ABOUT_S_load, x, y, self.canvas):
            self.canvas.delete('all')
            self.NAME = canvas.create_image(self.NAMEPic[1], self.NAMEPic[2], image=self.NAMEload)
            self.BACK = canvas.create_image(self.BACK_S[1], self.BACK_S[2], image=self.BACK_S_load)
            tk.bind('<Button-1>', menu.go_back)
            tk.bind('<Motion>', menu.motion_settings)
        elif Menu.inside(self.EXIT, self.EXIT_S_load, x, y, self.canvas):
            sys.exit()


    def go_back(self, event):
        x, y = event.x, event.y
        if Menu.inside(self.BACK, self.BACK_S_load, x, y, self.canvas):
            self.canvas.delete('all')
            self.NAME = canvas.create_image(self.NAMEPic[1], self.NAMEPic[2], image=self.NAMEload)
            self.START = canvas.create_image(self.START_S[1], self.START_S[2], image=self.START_S_load)
            self.SETTINGS = canvas.create_image(self.SETTINGS_S[1], self.SETTINGS_S[2], image=self.SETTINGS_S_load)
            self.ABOUT = canvas.create_image(self.ABOUT_S[1], self.ABOUT_S[2], image=self.ABOUT_S_load)
            self.EXIT = canvas.create_image(self.EXIT_S[1], self.EXIT_S[2], image=self.EXIT_S_load)
            tk.bind('<Button-1>', menu.go_to_menu)
            tk.bind('<Motion>', menu.motion_menu)
            tk.mainloop()


menu = Menu(canvas, 'menu')
tk.bind('<Motion>', menu.motion_menu)
tk.bind('<Button-1>', menu.go_to_menu)

tk.mainloop()
