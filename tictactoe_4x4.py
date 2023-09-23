from tkinter import *
import random



def create4x4board():

    def next_turns(row, column):
        global player

        if buttons[row][column]['text'] == "" and check_winners() is False:
            if player == players[0]:
                buttons[row][column]['text'] = player
                if check_winners() is False:
                    player = players[1]
                    label.config(text = ("Player " + players[1] + " turn"))
                elif check_winners() is True:
                    label.config(text = ("Player " + players[0] + " wins"))
                elif check_winners() == "Tie":
                    label.config(text = ("Tie!!"))

            else:
                buttons[row][column]['text'] = player
                if check_winners() is False:
                    player = players[0]
                    label.config(text = ("Player " + players[0] + " turn"))
                elif check_winners() is True:
                    label.config(text = ("Player " + players[1] + " wins"))
                elif check_winners() == "Tie":
                    label.config(text = ("Tie!!"))

    def check_winners():
        for row in range(4):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] == buttons[row][3]['text']!= "":
                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                buttons[row][3].config(bg="green")
                return True

        for column in range(4):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] == buttons[3][column]['text'] != "":
                buttons[0][column].config(bg="green")
                buttons[1][column].config(bg="green")
                buttons[2][column].config(bg="green")
                buttons[3][column].config(bg="green")
                return True

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == buttons[3][3]['text'] != "":
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            buttons[3][3].config(bg="green")
            return True

        elif buttons[0][3]['text'] == buttons[1][2]['text'] == buttons[2][1]['text'] == buttons[0][3]['text'] != "":
            buttons[0][3].config(bg="green")
            buttons[1][2].config(bg="green")
            buttons[2][1].config(bg="green")
            buttons[3][0].config(bg="green")
            return True

        elif empty_space() is False:

            for row in range(4):
                for column in range(4):
                    buttons[row][column].config(bg="yellow")
            return "Tie"

        else:
            return False

    def empty_space():

        spaces = 16

        for row in range(4):
            for column in range(4):
                if buttons[row][column]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def new_games():

        global player

        player = random.choice(players)

        label.config(text = "Player " + player + " turn")

        for row in range(4):
            for column in range(4):
                buttons[row][column].config(text="",bg="#F0F0F0")



    def threeboard():
    
        window.destroy()
        from tictactoe import create3x3board
        create3x3board()

    def fiveboard():
    
        window.destroy()
        from tictactoe_5x5 import create5x5board
        create5x5board()

    window = Tk()
    window.title("Tic-Tac-Toe")

    window.resizable(False, False)
    window_height = 500
    window_width = 900

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    menubar = Menu(window)
    window.config(menu = menubar)
    file_menu = Menu(menubar, tearoff = False)
    file_menu.add_command(label= 'Exit', command= window.destroy)
    menubar.add_cascade(label = "File", menu = file_menu)
    sub_menu = Menu(file_menu, tearoff = 0)
    sub_menu.add_command(label = '3x3 board', command = threeboard)
    sub_menu.add_command(label = '5x5 board', command = fiveboard)

        # add the File menu to the menubar
    file_menu.add_cascade(label = "Game Types", menu = sub_menu)
    global players, player
    players = ["x", "o"]
    player = random.choice(players)
    buttons = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    label_Title = Label(text = "Tic Tac Toe", font=('Helvetica bold', 26))
    label_Title.pack(side = "top")

    label = Label(text = "Player " + player + " turn")
    label.pack(side = "top")



    reset_button = Button(text = "Restart", command = new_games)
    reset_button.place(x = 50, y = 400)
  

    frame = Frame(window)
    frame.pack()

    for row in range(4):
        for column in range(4):
            buttons[row][column] = Button(frame, text="", width=5, height=2,
                                        command= lambda row=row, column=column: next_turns(row,column))
            buttons[row][column].grid(row=row,column=column)
    window.mainloop()











