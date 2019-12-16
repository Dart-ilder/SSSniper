from tkinter import *
from PIL import Image, ImageTk
import sys
import pygame
import game
from SSH_server import Server


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


# pygame.init()!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
pygame.mixer.init()

tk = Tk()
tk.title('Game')
tk.config(cursor='plus')
tk.configure(background=_from_rgb((235, 235, 235)))
tk.resizable(0, 0)

tk.wm_attributes('-topmost', 1)

WIDTH = 1200
HEIGHT = 800

MUSIC_VOLUME = 0.5
SOUNDS_VOLUME = 0.5
SENSITIVITY = 1
SETTINGS = [MUSIC_VOLUME, SOUNDS_VOLUME, SENSITIVITY]

canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
tk.update()

background_sound = pygame.mixer.music.load('Sounds/background.mp3')
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play()

music_volume = StringVar()
sounds_volume = StringVar()
sensitivity = StringVar()
music_volume_label = Label(text="Music volume:", font="Arial 16")
sounds_volume_label = Label(text="Sounds volume:", font="Arial 16")
sensitivity_label = Label(text="Sensitivity:", font="Arial 16")
music_labels = [music_volume_label, sounds_volume_label, sensitivity_label]
music_volume_entry = Entry(textvariable=music_volume)
sounds_volume_entry = Entry(textvariable=sounds_volume)
sensitivity_entry = Entry(textvariable=sensitivity)
music_entries = [music_volume_entry, sounds_volume_entry, sensitivity_entry]

server_host = StringVar()
server_port = StringVar()

server_host_label = Label(text="Присоединиться к другу:", font="Arial 16")
server_port_label = Label(text="Или ждём друга..", font="Arial 16")
multiplayer_labels = [server_host_label, server_port_label]
server_host_entry = Entry(textvariable=server_host_label)
server_port_entry = Entry(textvariable=server_port_label)

multiplayer_entries = [server_host_entry, server_port_entry]
MULTIPLAYER_SETTINGS = [server_host, server_port]


def settings_refresh(settings_list):
    pygame.mixer.music.set_volume(settings_list[0])


def multiplayer_settings(settings_list):
    if settings_list[0]:
        return [1, settings_list[0]]
    else:
        return [0, settings_list[1], settings_list[2]]


class Menu(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.menu_ident = 1

        self.NAME_Pic = ('Images/Menu resources/SSSniper.png', 620, 80)
        self.START_B = ('Images/Menu resources/start_b.png', 600, 300)
        self.START_S = ('Images/Menu resources/start_s.png', 600, 300)
        self.SETTINGS_B = ('Images/Menu resources/settings_b.png', 601, 400)
        self.SETTINGS_S = ('Images/Menu resources/settings_s.png', 601, 400)
        self.CHOOSE_B = ('Images/Menu resources/choose_b.png', 600, 540)
        self.CHOOSE_S = ('Images/Menu resources/choose_s.png', 600, 540)
        self.ABOUT_B = ('Images/Menu resources/about_b.png', 597, 490)
        self.ABOUT_S = ('Images/Menu resources/about_s.png', 597, 490)
        self.HOLE_Pic = ('Images/Menu resources/hole.png', -50, 700)
        self.BACK_B = ('Images/Menu resources/back_b.png', 30, 60)
        self.BACK_S = ('Images/Menu resources/back_s.png', 30, 60)
        self.EXIT_S = ('Images/Menu resources/exit_s.png', 600, 600)
        self.EXIT_B = ('Images/Menu resources/exit_b.png', 600, 600)
        self.CANCEL_S = ('Images/Menu resources/cancel_s.png', 750, 600)
        self.CANCEL_B = ('Images/Menu resources/cancel_b.png', 750, 600)
        self.SAVE_S = ('Images/Menu resources/save_s.png', 450, 600)
        self.SAVE_B = ('Images/Menu resources/save_b.png', 450, 600)
        self.SINGLEPLAYER_S = ('Images/Menu resources/singleplayer_s.png', 700, 350)
        self.SINGLEPLAYER_B = ('Images/Menu resources/singleplayer_b.png', 700, 350)
        self.MULTIPLAYER_S = ('Images/Menu resources/multiplayer_s.png', 725, 450)
        self.MULTIPLAYER_B = ('Images/Menu resources/multiplayer_b.png', 725, 450)
        self.INFO = ('Images/Menu resources/information.png', 600, 300)

        self.NAME_load = ImageTk.PhotoImage(Image.open(self.NAME_Pic[0]))
        self.CHOOSE_S_load = ImageTk.PhotoImage(Image.open(self.CHOOSE_S[0]))
        self.CHOOSE_B_load = ImageTk.PhotoImage(Image.open(self.CHOOSE_B[0]))
        self.SETTINGS_S_load = ImageTk.PhotoImage(Image.open(self.SETTINGS_S[0]))
        self.SETTINGS_B_load = ImageTk.PhotoImage(Image.open(self.SETTINGS_B[0]))
        self.START_S_load = ImageTk.PhotoImage(Image.open(self.START_S[0]))
        self.START_B_load = ImageTk.PhotoImage(Image.open(self.START_B[0]))
        self.ABOUT_B_load = ImageTk.PhotoImage(Image.open(self.ABOUT_B[0]))
        self.ABOUT_S_load = ImageTk.PhotoImage(Image.open(self.ABOUT_S[0]))
        self.HOLE_load = ImageTk.PhotoImage(Image.open(self.HOLE_Pic[0]))
        self.BACK_B_load = ImageTk.PhotoImage(Image.open(self.BACK_B[0]))
        self.BACK_S_load = ImageTk.PhotoImage(Image.open(self.BACK_S[0]))
        self.EXIT_S_load = ImageTk.PhotoImage(Image.open(self.EXIT_S[0]))
        self.EXIT_B_load = ImageTk.PhotoImage(Image.open(self.EXIT_B[0]))
        self.CANCEL_S_load = ImageTk.PhotoImage(Image.open(self.CANCEL_S[0]))
        self.CANCEL_B_load = ImageTk.PhotoImage(Image.open(self.CANCEL_B[0]))
        self.SAVE_S_load = ImageTk.PhotoImage(Image.open(self.SAVE_S[0]))
        self.SAVE_B_load = ImageTk.PhotoImage(Image.open(self.SAVE_B[0]))
        self.SINGLEPLAYER_S_load = ImageTk.PhotoImage(Image.open(self.SINGLEPLAYER_S[0]))
        self.SINGLEPLAYER_B_load = ImageTk.PhotoImage(Image.open(self.SINGLEPLAYER_B[0]))
        self.MULTIPLAYER_S_load = ImageTk.PhotoImage(Image.open(self.MULTIPLAYER_S[0]))
        self.MULTIPLAYER_B_load = ImageTk.PhotoImage(Image.open(self.MULTIPLAYER_B[0]))
        self.INFO_load = ImageTk.PhotoImage(Image.open(self.INFO[0]))

        self.NAME = canvas.create_image(self.NAME_Pic[1], self.NAME_Pic[2], image=self.NAME_load)
        self.START = canvas.create_image(self.START_S[1], self.START_S[2], image=self.START_S_load)
        self.SETTINGS = canvas.create_image(self.SETTINGS_S[1], self.SETTINGS_S[2], image=self.SETTINGS_S_load)
        self.ABOUT = canvas.create_image(self.ABOUT_S[1], self.ABOUT_S[2], image=self.ABOUT_S_load)
        self.EXIT = canvas.create_image(self.EXIT_S[1], self.EXIT_S[2], image=self.EXIT_S_load)
        self.HOLE = ''
        self.BACK = ''
        self.CANCEL = ''
        self.SAVE = ''
        self.SINGLEPLAYER = ''
        self.MULTIPLAYER = ''

        self.previous_menu_branch = ""
        canvas.update()

    def mouse_inside_pic(obj, obj_s_load, x, y, canvas):
        if canvas.coords(obj)[0] - obj_s_load.width() * 0.5 < x < canvas.coords(obj)[
            0] + obj_s_load.width() * 0.5 and canvas.coords(obj)[
            1] - obj_s_load.height() * 0.5 < y < canvas.coords(obj)[
            1] + obj_s_load.height() * 0.5:
            return True
        else:
            return False

    def pic_change(obj, x, y, canvas, obj_s_load, obj_b_load, obj_s, obj_b):
        if Menu.mouse_inside_pic(obj, obj_s_load, x, y, canvas):
            canvas.delete(obj)
            obj_returned = canvas.create_image(obj_b[1], obj_b[2], image=obj_b_load)
        else:
            canvas.delete(obj)
            obj_returned = canvas.create_image(obj_s[1], obj_s[2], image=obj_s_load)
        return obj_returned

    def main_menu(self):
        self.NAME = canvas.create_image(self.NAME_Pic[1], self.NAME_Pic[2], image=self.NAME_load)
        self.START = canvas.create_image(self.START_S[1], self.START_S[2], image=self.START_S_load)
        self.SETTINGS = canvas.create_image(self.SETTINGS_S[1], self.SETTINGS_S[2], image=self.SETTINGS_S_load)
        self.ABOUT = canvas.create_image(self.ABOUT_S[1], self.ABOUT_S[2], image=self.ABOUT_S_load)
        self.EXIT = canvas.create_image(self.EXIT_S[1], self.EXIT_S[2], image=self.EXIT_S_load)
        tk.bind('<Button-1>', self.main_menu_tree)
        tk.bind('<Motion>', self.main_menu_mouse_motion)

    def main_menu_mouse_motion(self, event):
        self.START = Menu.pic_change(self.START, event.x, event.y, canvas, self.START_S_load, self.START_B_load,
                                     self.START_S, self.START_B)
        self.SETTINGS = Menu.pic_change(self.SETTINGS, event.x, event.y, canvas, self.SETTINGS_S_load,
                                        self.SETTINGS_B_load, self.SETTINGS_S, self.SETTINGS_B)
        self.ABOUT = Menu.pic_change(self.ABOUT, event.x, event.y, canvas, self.ABOUT_S_load, self.ABOUT_B_load,
                                     self.ABOUT_S, self.ABOUT_B)
        self.EXIT = Menu.pic_change(self.EXIT, event.x, event.y, canvas, self.EXIT_S_load, self.EXIT_B_load,
                                    self.EXIT_S, self.EXIT_B)

    def start_menu(self):
        self.NAME = canvas.create_image(self.NAME_Pic[1], self.NAME_Pic[2], image=self.NAME_load)
        self.HOLE = canvas.create_image(self.HOLE_Pic[1], self.HOLE_Pic[2], image=self.HOLE_load)
        self.BACK = canvas.create_image(self.BACK_S[1], self.BACK_S[2], image=self.BACK_S_load)
        self.SINGLEPLAYER = canvas.create_image(self.SINGLEPLAYER_S[1], self.SINGLEPLAYER_S[2],
                                                image=self.SINGLEPLAYER_S_load)
        self.MULTIPLAYER = canvas.create_image(self.MULTIPLAYER_S[1], self.MULTIPLAYER_S[2],
                                               image=self.MULTIPLAYER_S_load)
        self.previous_menu_branch = "main_menu"
        tk.bind('<Motion>', self.start_menu_mouse_motion)
        tk.bind('<Button-1>', self.start_menu_tree)

    def start_menu_mouse_motion(self, event):
        if self.menu_ident:
            x, y = event.x, event.y
            self.BACK = Menu.pic_change(self.BACK, x, y, canvas, self.BACK_S_load, self.BACK_B_load, self.BACK_S,
                                        self.BACK_B)
            self.SINGLEPLAYER = Menu.pic_change(self.SINGLEPLAYER, x, y, canvas, self.SINGLEPLAYER_S_load,
                                                self.SINGLEPLAYER_B_load, self.SINGLEPLAYER_S, self.SINGLEPLAYER_B)
            self.MULTIPLAYER = Menu.pic_change(self.MULTIPLAYER, x, y, canvas, self.MULTIPLAYER_S_load,
                                               self.MULTIPLAYER_B_load, self.MULTIPLAYER_S, self.MULTIPLAYER_B)

    def settings_menu(self):
        self.NAME = canvas.create_image(self.NAME_Pic[1], self.NAME_Pic[2], image=self.NAME_load)
        self.CANCEL = canvas.create_image(self.CANCEL_S[1], self.CANCEL_S[2], image=self.CANCEL_S_load)
        self.SAVE = canvas.create_image(self.SAVE_S[1], self.SAVE_S[2], image=self.SAVE_S_load)
        self.BACK = canvas.create_image(self.BACK_S[1], self.BACK_S[2], image=self.BACK_S_load)
        self.previous_menu_branch = "main_menu"
        music_volume_label.place(relx=.35, rely=.4)
        sounds_volume_label.place(relx=.35, rely=.5)
        sensitivity_label.place(relx=.35, rely=.6)
        music_volume_entry.place(relx=.55, rely=.41)
        sounds_volume_entry.place(relx=.55, rely=.51)
        sensitivity_entry.place(relx=.55, rely=.61)
        for i in range(0, len(music_entries)):
            music_entries[i].insert(0, int(SETTINGS[i] * 100))
        tk.bind('<Button-1>', menu.click)
        tk.bind('<Motion>', menu.settings_menu_mouse_motion)

    def settings_menu_mouse_motion(self, event):
        x, y = event.x, event.y
        self.CANCEL = Menu.pic_change(self.CANCEL, x, y, canvas, self.CANCEL_S_load, self.CANCEL_B_load, self.CANCEL_S,
                                      self.CANCEL_B)
        self.SAVE = Menu.pic_change(self.SAVE, x, y, canvas, self.SAVE_S_load, self.SAVE_B_load, self.SAVE_S,
                                    self.SAVE_B)
        self.BACK = Menu.pic_change(self.BACK, x, y, canvas, self.BACK_S_load, self.BACK_B_load, self.BACK_S,
                                    self.BACK_B)

    def about_menu(self):
        self.NAME = canvas.create_image(self.NAME_Pic[1], self.NAME_Pic[2], image=self.NAME_load)
        self.INFORMATION = canvas.create_image(self.INFO[1], self.INFO[2], image=self.INFO_load)
        self.BACK = canvas.create_image(self.BACK_S[1], self.BACK_S[2], image=self.BACK_S_load)
        self.previous_menu_branch = "main_menu"
        tk.bind('<Motion>', self.about_menu_mouse_motion)
        tk.bind('<Button-1>', self.click)

    def about_menu_mouse_motion(self, event):
        x, y = event.x, event.y
        self.BACK = Menu.pic_change(self.BACK, x, y, canvas, self.BACK_S_load, self.BACK_B_load, self.BACK_S,
                                    self.BACK_B)

    def server_settings_menu(self):
        self.NAME = canvas.create_image(self.NAME_Pic[1], self.NAME_Pic[2], image=self.NAME_load)
        self.CANCEL = canvas.create_image(self.CANCEL_S[1], self.CANCEL_S[2], image=self.CANCEL_S_load)
        self.SAVE = canvas.create_image(self.SAVE_S[1], self.SAVE_S[2], image=self.SAVE_S_load)
        self.BACK = 0
        self.previous_menu_branch = "start_menu"
        server_host_label.place(relx=.35, rely=.40)
        server_port_label.place(relx=.35, rely=.45)
        server_port_entry.place(relx=.55, rely=.45)
        server_host_entry.place(relx=.55, rely=.40)

        tk.bind('<Button-1>', menu.click)
        tk.bind('<Motion>', menu.server_settings_menu_mouse_motion)

    def server_settings_menu_mouse_motion(self, event):
        x, y = event.x, event.y
        self.CANCEL = Menu.pic_change(self.CANCEL, x, y, canvas, self.CANCEL_S_load, self.CANCEL_B_load, self.CANCEL_S,
                                      self.CANCEL_B)
        self.SAVE = Menu.pic_change(self.SAVE, x, y, canvas, self.SAVE_S_load, self.SAVE_B_load, self.SAVE_S,
                                    self.SAVE_B)

    def main_menu_tree(self, event):
        x, y = event.x, event.y
        if Menu.mouse_inside_pic(self.START, self.START_S_load, x, y, self.canvas):
            self.canvas.delete('all')
            self.start_menu()
        elif Menu.mouse_inside_pic(self.SETTINGS, self.SETTINGS_S_load, x, y, self.canvas):
            self.canvas.delete('all')
            self.settings_menu()
        elif Menu.mouse_inside_pic(self.ABOUT, self.ABOUT_S_load, x, y, self.canvas):
            self.canvas.delete('all')
            self.about_menu()
        elif Menu.mouse_inside_pic(self.EXIT, self.EXIT_S_load, x, y, self.canvas):
            sys.exit()

    def start_menu_tree(self, event): 
        # 'дерево' перехода из start_menu 
        if self.menu_ident: 
            x, y = event.x, event.y 
            if Menu.mouse_inside_pic(self.SINGLEPLAYER, self.SINGLEPLAYER_S_load, x, y, self.canvas): 
                self.canvas.delete('all')
                self.menu_ident = 0 
                game.game_process(tk, canvas) 
            elif Menu.mouse_inside_pic(self.MULTIPLAYER, self.MULTIPLAYER_S_load, x, y, self.canvas): 
                self.canvas.delete('all') 
                self.server_settings_menu() 
            elif Menu.mouse_inside_pic(self.BACK, self.BACK_S_load, x, y, self.canvas): 
                self.canvas.delete('all') 
                self.BACK = 0 
                self.main_menu()

    def click(self, event):
        x, y = event.x, event.y
        if self.BACK:
            if Menu.mouse_inside_pic(self.BACK, self.BACK_S_load, x, y, self.canvas):
                self.canvas.delete('all')
                self.BACK = 0
                self.SAVE = 0
                if self.previous_menu_branch == "main_menu":
                    for i in range(0, len(music_labels)):
                        music_labels[i].place_forget()
                    for i in range(0, len(music_entries)):
                        music_entries[i].delete(0, END)
                        music_entries[i].place_forget()
                    self.main_menu()
                if self.previous_menu_branch == "start_menu":
                    for i in range(0, len(multiplayer_labels)):
                        multiplayer_labels[i].place_forget()
                    for i in range(0, len(multiplayer_entries)):
                        multiplayer_entries[i].delete(0, END)
                        multiplayer_entries[i].place_forget()
                    self.start_menu()
        if self.CANCEL:
            print(canvas.coords(self.CANCEL))
            if Menu.mouse_inside_pic(self.CANCEL, self.CANCEL_S_load, x, y, self.canvas):
                self.canvas.delete('all')
                self.CANCEL = 0
                self.SAVE = 0
                if self.previous_menu_branch == "main_menu":
                    for i in range(0, len(music_labels)):
                        music_labels[i].place_forget()
                    for i in range(0, len(music_entries)):
                        music_entries[i].delete(0, END)
                        music_entries[i].place_forget()
                    self.main_menu()
                if self.previous_menu_branch == "start_menu":
                    for i in range(0, len(multiplayer_labels)):
                        multiplayer_labels[i].place_forget()
                    for i in range(0, len(multiplayer_entries)):
                        multiplayer_entries[i].delete(0, END)
                        multiplayer_entries[i].place_forget()
                    self.start_menu()
        if self.SAVE:
            if Menu.mouse_inside_pic(self.SAVE, self.SAVE_S_load, x, y, self.canvas):
                if self.previous_menu_branch == "main_menu":
                    for i in range(0, len(music_entries)):
                        if music_entries[i].get():
                            SETTINGS[i] = int(music_entries[i].get()) / 100
                            print(SETTINGS[i])
                            settings_refresh(SETTINGS)
                if self.previous_menu_branch == "start_menu":
                    if multiplayer_entries[0].get():
                        MULTIPLAYER_SETTINGS[0] = multiplayer_entries[0].get()
                        print(MULTIPLAYER_SETTINGS[0])
                        server = Server(multiplayer_settings(MULTIPLAYER_SETTINGS)[0], 'first')
                    elif multiplayer_entries[1].get():
                        MULTIPLAYER_SETTINGS[1] = multiplayer_entries[1].get()
                        print(MULTIPLAYER_SETTINGS[1])
                        server = Server(multiplayer_settings(MULTIPLAYER_SETTINGS)[1], 'second')
                    else:
                        pass


menu = Menu(canvas)
tk.bind('<Motion>', menu.main_menu_mouse_motion)
tk.bind('<Button-1>', menu.main_menu_tree)

tk.mainloop()
