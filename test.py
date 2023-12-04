import customtkinter as ctk
import subprocess
import tkinter
import os
from PIL import ImageTk, Image

Landing_page = ctk.CTk()
Landing_page.title('Arcade')
Landing_page.geometry('1366x768')

def login_page():
    frame = ctk.CTkFrame(   
        master = Landing_page,
        height = 500,
        width = 500,
        corner_radius = 50,
        fg_color = '#171717',
        border_width = 8,
        border_color = '#DA0037'
        )
    frame.place(
        relx = 0.5, 
        rely = 0.5,
        anchor=tkinter.CENTER)
    # ------------------------------------------------------------------------------------------------------------------------------------
    def login_Interface():
        global user_Entry, pass_Entry
        login_Frame = ctk.CTkFrame(
            master = frame,
            height = 600,
            width = 800,
            corner_radius = 50,
            fg_color = '#262626',
            border_width = 10,
            border_color = '#F8C8C8'
        )
        login_Frame.place(
            relx = 0.5,
            rely = 0.5,
            anchor = tkinter.CENTER
        )

        log_Acc = ctk.CTkLabel(
            master = login_Frame,
            text = 'Login to your Account',
            font = ('Ubuntu', 20, 'bold')
        )
        log_Acc.place(
            x = 58,
            y = 100
        )

        app_Welcome = ctk.CTkLabel(
            master = login_Frame,
            text = 'Welcome to Arcade Games!',
            font = ('Alpharush - Retro Gaming Typeface', 25, 'bold')
        )
        app_Welcome.place(
            x = 58,
            y = 45
        )

        enter_User = ctk.CTkLabel(
            master = login_Frame,
            text = 'Username',
            font = ('Ubuntu', 15)
        )
        enter_User.place(
            x = 58,
            y = 155
        )

        user_Entry = ctk.CTkEntry(
            login_Frame,
            height = 40,
            width = 250,
            placeholder_text = 'Enter your Username'
        )
        user_Entry.place(
            x = 58,
            y = 185
        )

        enter_Pass = ctk.CTkLabel(
            master = login_Frame,
            text = 'Password',
            font = ('Ubuntu', 15)
        )
        enter_Pass.place(
            x = 58,
            y = 240
        )

        pass_Entry = ctk.CTkEntry(
            login_Frame,
            height = 40,
            width = 250,
            placeholder_text = 'Enter your Password',
            show = '*'
        )
        pass_Entry.place(
            x = 58,
            y = 270
        )

        login_Button = ctk.CTkButton(
            login_Frame,
            fg_color = "#F8C8C8",
            text_color = "#000000",
            height = 35,
            width = 90,
            text = 'Login',
            font = ('Ubuntu', 15, 'bold'),
            command = authentication
        )
        login_Button.place(
            x = 139,
            y = 340
        )

        no_Acc = ctk.CTkLabel(
            login_Frame,
            text = 'No Account?',
            font = ("Helvetica", 12)
        )
        no_Acc.place(
            x = 90,
            y = 400
        )

        registeracc_button = ctk.CTkButton(
            login_Frame,
            fg_color = "transparent",
            text_color = "#F8C8C8",
            height = 35,
            width = 30,
            text = 'Create a New One',
            font = ('Helvetica', 12,'bold'),
            command = register_Acc
        )
        registeracc_button.place(
            x = 160,
            y = 397.5
        )

    # Create User Account Interface
    def register_Acc():
        register_Frame = ctk.CTkFrame(
            master = Landing_page,
            height = 600,
            width = 800,
            corner_radius = 50,
            fg_color = '#262626',
            border_width = 10,
            border_color = '#F8C8C8'
        )
        register_Frame.place(
            relx = 0.5,
            rely = 0.5,
            anchor = tkinter.CENTER
        )

        app_Welcome = ctk.CTkLabel(
            master = register_Frame,
            text = 'Welcome to Arcade Games!',
            font = ('Alpharush - Retro Gaming Typeface', 25, 'bold')
        )
        app_Welcome.place(
            x = 58,
            y = 45
        )

        create_Acc = ctk.CTkLabel(
            master = register_Frame,
            text = 'Create your Account',
            font = ('Ubuntu', 20, 'bold')
        )
        create_Acc.place(
            x = 58,
            y = 100
        )

        enter_Uniqueuser = ctk.CTkLabel(
            master = register_Frame,
            text = 'Enter Unique Username',
            font = ('Ubuntu', 15)
        )
        enter_Uniqueuser.place(
            x = 58,
            y = 155
        )

        enter_Newuser = ctk.CTkEntry(
            register_Frame,
            height = 40,
            width = 250,
            placeholder_text = 'Create your Username'
        )
        enter_Newuser.place(
            x = 58,
            y = 185
        )

        enter_Uniquepass = ctk.CTkLabel(
            master = register_Frame,
            text = 'Enter Password',
            font = ('Ubuntu', 15)
        )
        enter_Uniquepass.place(
            x = 58,
            y = 240
        )

        enter_Newpass = ctk.CTkEntry(
            register_Frame,
            height = 40,
            width = 250,
            placeholder_text = 'Create your Password',
            show = '*'
        )
        enter_Newpass.place(
            x = 58,
            y = 270
        )

    # Function to write the newly created acc in the CSV file database
    def write_NewUser():
        user_input = enter_Newuser.get()
        pass_input = enter_Newpass.get()

        if user_Exist(user_input):
            print('Username already taken. Please choose another one.')
        else:
            data_to_append = [[user_input,  pass_input]]
            file = open('userinfo.csv', 'a', newline = '')
            writer = csv.writer(file)

            writer.writerows(data_to_append)

            file.close()

        login_Interface()

    create_Button = ctk.CTkButton(
        register_Frame,
        fg_color = "#F8C8C8",
        text_color = "#000000",
        height = 35,
        width = 90,
        text = 'Create',
        font = ('Ubuntu', 15, 'bold'),
        command = write_NewUser
    )
    create_Button.place(
        x = 139,
        y = 340
    )

    have_Acc = ctk.CTkLabel(
        register_Frame,
        text = 'Already have Account?',
        font = ("Helvetica", 12)
    )
    have_Acc.place(
        x = 90,
        y = 400
    )

    signin_Button = ctk.CTkButton(
        register_Frame,
        fg_color = "transparent",
        text_color = "#F8C8C8",
        height = 35,
        width = 30,
        text = 'Sign In',
        font = ('Helvetica', 12,'bold'),
        command = sign_In
    )
    signin_Button.place(
        x = 220,
        y = 397.5
    )

    # Function to call again the Login Interface during creating an account
    def sign_In():
        login_Interface()

    # Function to read the user data in the CSV File.
    def read_User():
        try:
            userData = pd.read_csv('userinfo.csv')
            userData['Password'] = userData['Password'].astype(str)
            return userData
        except FileNotFoundError:
            print("User data file not found.")
            return None

    # Function to know if the username input during creation of account is already existed
    def user_Exist(username):
        global userData
        if userData is not None:
            taken_Usernames = userData['Username'].tolist()
            return username in taken_Usernames
        else:
            return False

    # Function to check if the username and password was matched in the CSV file
    def authenticate_User(username, password):
        global userData
        if userData is not None:
            matches = userData.index[(userData.Username == username) & (userData.Password == password)].tolist()
            return matches 
        else: 
            return False

    # Function to know if the user was successfully log in ang goes directly to the homepage of the game
    def authentication():
        global userData
        username = user_Entry.get()
        password = pass_Entry.get()
        print(username, password)

        authenticated = authenticate_User(username, password)

        if authenticated:
            print('Login successful!')
        else:
            print('Invalid username or password. Please try again.')

    # Reads the CSV file
    userData = read_User()
    print(userData)

def start_button_event():
    Landing_page.destroy()
    homepage = ctk.CTk()
    homepage.geometry('1366x768')
    homepage.title('Arcade')
    #FRAME, LOGOUT, INTRO LABEL ------------------------------------------------------------------------------------------------------------------------------------
    frame = ctk.CTkFrame(
        master = homepage,
        height = 150,
        width = 900,
        fg_color = 'black',
        corner_radius = 15,
        border_width = 8,
        border_color = ('#7743DB', '#DA0037')  
        )
    frame.place(
        x = 240,
        y = 30)

    logout = ctk.CTkButton(
        master = frame,
        text = 'logout',
        command = login_page
    )
    logout.place(
        x = 10,
        y = 30
    )
    Intro = ctk.CTkLabel(
        master = frame,
        text = 'Welcome to the Arcade Collection!',
        font = ('Ubuntu', 50, 'bold'))
    Intro.place(
        x = 40,
        y = 50)
 # ------------------------------------------------------------------------------------------------------------------------------------   # Eto ung reason bakit tayo nag import ng PIL or pillow sa taas kasi eto ung module na ginagamit sa python if may images na involved
    flappy_banner = ctk.CTkImage(
        Image.open("Flappy Bird\Flappy bird banner.png"),
        size = (300,400)
        )

    hungry_snake_banner = ctk.CTkImage(
        Image.open("Hungry Snake\hungry snake banner.png"),
        size = (300,400)
        )
    # GAME FRAMES ------------------------------------------------------------------------------------------------------------------------------------
    game_collection_frame = ctk.CTkScrollableFrame(
        master = homepage,
        width = 1100,
        height = 500,
        fg_color = 'transparent',
        scrollbar_button_color = ('#7743DB', '#DA0037') 
        )
    game_collection_frame.place(
        x = 130,
        y = 220,)

    game_frame1 = ctk.CTkFrame(
        master = game_collection_frame,
        height = 400,
        width = 1000,
        fg_color = 'transparent' 
        )
    game_frame1.pack(
        pady = 10
        )

    game_frame2 = ctk.CTkFrame(
        master = game_collection_frame,
        height = 400,
        width = 1000,
        fg_color = 'transparent' 
        )
    game_frame2.pack(
        pady = 10
        )
    
    game_frame3 = ctk.CTkFrame(
        master = game_collection_frame,
        height = 400,
        width = 1000,
        fg_color = 'transparent' 
        )
    game_frame3.pack(
        pady = 10
        )

    #GAME EVENTS ------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------
    def game1_event():
        os.startfile('Hungry Snake\Snake.exe')

    game1 = ctk.CTkButton(
        master = game_frame1,
        height = 400,
        width = 300,
        fg_color = ('#7743DB', '#DA0037'),
        hover_color = ('#3b216d', '#8e0024'),
        command = game1_event,
        image = hungry_snake_banner,
        text = '' )

    game1.pack(
        side = 'left',
        padx = 20        )
    # ------------------------------------------------------------------------------------------------------------------------------------
    def game2_event():
        folder_path = 'Flappy Bird\dist'
        file_name = 'Flappy.exe'
        file_path = os.path.join(folder_path, file_name)

        if os.path.exists(file_path):
          subprocess.run(file_path)
        else:
          print(f"The file {file_name} does not exist in the folder {folder_path}.")

    game2 = ctk.CTkButton(
        master = game_frame1,
        height = 400,
        width = 300,
        fg_color = ('#7743DB', '#DA0037'),
        hover_color = ('#3b216d', '#8e0024'),
        command = game2_event,
        image = flappy_banner,
        text = '')
    game2.pack(
        side = 'right',
        padx = 20        )
    # ------------------------------------------------------------------------------------------------------------------------------------
    def game3_event():
        os.startfile('2048\dist\Game_2048.exe') 

    game3 = ctk.CTkButton(
        master = game_frame1,
        height = 400,
        width = 300,
        fg_color = ('#7743DB', '#DA0037'),
        hover_color = ('#3b216d', '#8e0024'),
        text = '2048',
        command = game3_event)
    game3.pack(
        side = 'right',
        padx = 20    )
    # ------------------------------------------------------------------------------------------------------------------------------------
    def game4_event():
        # os.startfile('') 
        pass
    
    game4 = ctk.CTkButton(
        master = game_frame2,
        height = 400,
        width = 300,
        fg_color = ('#7743DB', '#DA0037'),
        hover_color = ('#3b216d', '#8e0024'),
        text = '',
        command = game4_event)
    game4.pack(
        side = 'left',
        padx = 20        )
    # ------------------------------------------------------------------------------------------------------------------------------------
    def game5_event():
        # os.startfile('') 
        pass
    
    game5 = ctk.CTkButton(
        master = game_frame2,
        height = 400,
        width = 300,
        fg_color = ('#7743DB', '#DA0037'),
        hover_color = ('#3b216d', '#8e0024'),
        text = '',
        command = game5_event )
    game5.pack(
        side = 'right',
        padx = 20        )
    # ------------------------------------------------------------------------------------------------------------------------------------
    def game6_event():
        # os.startfile('') 
        pass
    
    game6 = ctk.CTkButton(
        master = game_frame2,
        height = 400,
        width = 300,
        fg_color = ('#7743DB', '#DA0037'),
        hover_color = ('#3b216d', '#8e0024'),
        text = '',
        command = game6_event )
    game6.pack(
        side = 'right',
        padx = 20    )
    # ------------------------------------------------------------------------------------------------------------------------------------
    def game7_event():
        # os.startfile('') 
        pass

    game7 = ctk.CTkButton(
        master = game_frame3,
        height = 400,
        width = 300,
        fg_color = ('#7743DB', '#DA0037'),
        hover_color = ('#3b216d', '#8e0024'),
        text = '',
        command = game7_event)
    game7.pack(
        side = 'left',
        padx = 20        )
    # ------------------------------------------------------------------------------------------------------------------------------------
    def game8_event():
       # os.startfile('') 
        pass
    
    game8 = ctk.CTkButton(
        master = game_frame3,
        height = 400,
        width = 300,
        fg_color = ('#7743DB', '#DA0037'),
        hover_color = ('#3b216d', '#8e0024'),
        text = '',
        command = game8_event )
    game8.pack(
        side = 'right',
        padx = 20        )
    # ------------------------------------------------------------------------------------------------------------------------------------
    def game9_event():
        # os.startfile('') 
        pass
    
    game9 = ctk.CTkButton(
        master = game_frame3,
        height = 400,
        width = 300,
        fg_color = ('#7743DB', '#DA0037'),
        hover_color = ('#3b216d', '#8e0024'),
        text = '',
        command = game9_event)
    game9.pack(
        side = 'right',
        padx = 20    )
    # ------------------------------------------------------------------------------------------------------------------------------------
    # LIGHT AND DARK MODE SWITCH------------------------------------------------------------------------------------------------------------------------------------
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
        offvalue = 'off')
    mode_switch.place(
        x = 25,
        y = 670)
    # main loop------------------------------------------------------------------------------------------------------------------------------------
    homepage.mainloop()

login_page()
Landing_page.mainloop()