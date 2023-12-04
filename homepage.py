import customtkinter as ctk
import tkinter
import os
from PIL import ImageTk, Image

homepage = ctk.CTk()
homepage.geometry('1366x768')
homepage.title('Arcade')

frame = ctk.CTkFrame(
    master = homepage,
    height = 150,
    width = 900,
    fg_color = 'transparent',
    corner_radius = 15,
    border_width = 8,
    border_color = ('#7743DB', '#DA0037')  
    )
frame.place(
    x = 240,
    y = 30)

Intro = ctk.CTkLabel(
    master = frame,
    text = 'Welcome to the Arcade Collection!',
    font = ('Ubuntu', 50, 'bold'))
Intro.place(
    x = 40,
    y = 50)

game_collection_frame = ctk.CTkScrollableFrame(
    master = homepage,
    width = 1100,
    height = 500,
    fg_color = 'transparent',
    scrollbar_button_color = ('#7743DB', '#DA0037') 
    )
game_collection_frame.place(
    x = 130,
    y = 220,
)
# ------------------------------------------------------------------------------------------------------------------------------------
flappy_banner = ImageTk.PhotoImage(Image.open("D:\programmmms\DSA APP\Flappy Bird\FlapPyBird-DSA-master\Flappy bird banner.png"))

# ------------------------------------------------------------------------------------------------------------------------------------
game_frame1 = ctk.CTkFrame(
    master = game_collection_frame,
    height = 400,
    width = 1000,
    fg_color = 'transparent' 
    )
game_frame1.pack(
    pady = 10
    )

def game1_event():
    os.startfile('D:\programmmms\DSA APP\Hungry Snake\Snake.exe')

game1 = ctk.CTkButton(
    master = game_frame1,
    height = 400,
    width = 300,
    fg_color = ('#7743DB', '#DA0037'),
    hover_color = ('#3b216d', '#8e0024'),
    command = game1_event )
game1.pack(
    side = 'left',
    padx = 20        )

def game2_event():
    os.startfile('D:\programmmms\DSA APP\Flappy Bird\FlapPyBird-DSA-master\Flappy.exe') 

game2 = ctk.CTkButton(
    master = game_frame1,
    height = 400,
    width = 300,
    fg_color = ('#7743DB', '#DA0037'),
    hover_color = ('#3b216d', '#8e0024'),
    command = game2_event,
    image = flappy_banner,)
game2.pack(
    side = 'right',
    padx = 20        )

game3 = ctk.CTkButton(
    master = game_frame1,
    height = 400,
    width = 300,
    fg_color = ('#7743DB', '#DA0037'),
    hover_color = ('#3b216d', '#8e0024') )
game3.pack(
    side = 'right',
    padx = 20    )
# ------------------------------------------------------------------------------------------------------------------------------------
game_frame2 = ctk.CTkFrame(
    master = game_collection_frame,
    height = 400,
    width = 1000,
    fg_color = 'transparent' 
    )
game_frame2.pack(
    pady = 10
    )

game4 = ctk.CTkButton(
    master = game_frame2,
    height = 400,
    width = 300,
    fg_color = ('#7743DB', '#DA0037'),
    hover_color = ('#3b216d', '#8e0024') )
game4.pack(
    side = 'left',
    padx = 20        )

game5 = ctk.CTkButton(
    master = game_frame2,
    height = 400,
    width = 300,
    fg_color = ('#7743DB', '#DA0037'),
    hover_color = ('#3b216d', '#8e0024') )
game5.pack(
    side = 'right',
    padx = 20        )

game6 = ctk.CTkButton(
    master = game_frame2,
    height = 400,
    width = 300,
    fg_color = ('#7743DB', '#DA0037'),
    hover_color = ('#3b216d', '#8e0024') )
game6.pack(
    side = 'right',
    padx = 20    )
# ------------------------------------------------------------------------------------------------------------------------------------
game_frame3 = ctk.CTkFrame(
    master = game_collection_frame,
    height = 400,
    width = 1000,
    fg_color = 'transparent' 
    )
game_frame3.pack(
    pady = 10
    )

game7 = ctk.CTkButton(
    master = game_frame3,
    height = 400,
    width = 300,
    fg_color = ('#7743DB', '#DA0037'),
    hover_color = ('#3b216d', '#8e0024'))
game7.pack(
    side = 'left',
    padx = 20        )

game8 = ctk.CTkButton(
    master = game_frame3,
    height = 400,
    width = 300,
    fg_color = ('#7743DB', '#DA0037'),
    hover_color = ('#3b216d', '#8e0024'))
game8.pack(
    side = 'right',
    padx = 20        )

game9 = ctk.CTkButton(
    master = game_frame3,
    height = 400,
    width = 300,
    fg_color = ('#7743DB', '#DA0037'),
    hover_color = ('#3b216d', '#8e0024'))
game9.pack(
    side = 'right',
    padx = 20    )


def mode_event():
    if switch_var.get() == 'on':
        ctk.set_appearance_mode("light")
    else: 
        ctk.set_appearance_mode("dark")

switch_var = ctk.StringVar(value='on')

mode_switch = ctk.CTkSwitch(
    master = homepage,
    text = 'Change Mode',
    command = mode_event,
    variable = switch_var,
    onvalue = 'on',
    offvalue = 'off'
)
mode_switch.place(
    x = 25,
    y = 670
)


homepage.mainloop()