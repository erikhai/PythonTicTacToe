from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter import messagebox
import random



def create3x3board():
    global players, player
    global xPlayerWins, yPlayerWins
    xPlayerWins = 0
    yPlayerWins = 0

    def next_turn(row, column):
        global player
        global xPlayerWins, yPlayerWins
        if buttons[row][column]['text'] == "" and check_winner() is False:
            if player == players[0]:
                buttons[row][column]['text'] = player
                if check_winner() is False:
                    player = players[1]
                    label.config(text = ("Player " + players[1] + " turn"))
                elif check_winner() is True:
                    label.config(text = ("Player " + players[0] + " wins"))
                    xPlayerWins += 1
                    playerXWins = Label(text = "Player " + players[0] + " wins: " + str(xPlayerWins))
                    playerXWins.place(x = 50, y = 100)
                    
                elif check_winner() == "Tie":
                    label.config(text = ("Tie!!"))

            else:
                buttons[row][column]['text'] = player
                if check_winner() is False:
                    player = players[0]
                    label.config(text = ("Player " + players[0] + " turn"))
                elif check_winner() is True:
                    label.config(text = ("Player " + players[1] + " wins"))
                    yPlayerWins += 1
                    playerYWins = Label(text = "Player " + players[1] + " wins: " + str(yPlayerWins))
                    playerYWins.place(x = 50, y = 130)
                elif check_winner() == "Tie":
                    label.config(text = ("Tie!!"))

    def check_winner():
        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                return True

        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                buttons[0][column].config(bg="green")
                buttons[1][column].config(bg="green")
                buttons[2][column].config(bg="green")
                return True

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True

        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            return True

        elif empty_spaces() is False:

            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="blue")
            return "Tie"

        else:
            return False

    def empty_spaces():

        spaces = 9

        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True
    def clear_data():
        playerXWins = Label(text = "Player " + players[0] + " wins: " + str(0))
        playerXWins.place(x = 50, y = 100)
        playerYWins = Label(text = "Player " + players[1] + " wins: " + str(0))
        playerYWins.place(x = 50, y = 130)
        new_game()
    def information_box():
        messagebox.showinfo("How to use this application", "This application will allow you to play a game of tic-tac-toe. You win the game by getting three marks either vertically, horiontally or diagonally. The game also keeps track of each players score which can be reset in the menu.")


    def new_game():

        global player

        player = random.choice(players)
        xPlayerWins = 0
        yPlayerWins = 0

        label.config(text = "Player " + player + " turn")

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="",bg="#F0F0F0")


 
    def show_settings():
        messagebox.showinfo("Settings", "This is the settings menu.")

    def show_sub_menu_item1():
        messagebox.showinfo("Submenu Item 1", "This is submenu item 1.")

    def show_sub_menu_item2():
        messagebox.showinfo("Submenu Item 2", "This is submenu item 2.")

    




    window = Tk()
    window.title("Tic-Tac-Toe")

    window.resizable(False, False)
    window_height = 700

    window_width = 900
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    menubar = Menu(window)
    window.config(menu = menubar)
    file_menu = Menu(menubar, tearoff = False)
    file_menu.add_command(label= 'Clear Game Scores', command= clear_data)
    file_menu.add_command(label= 'How This Application Works', command= information_box)
    setting_submenu = Menu(file_menu, tearoff = False)
    setting_submenu.add_command(label="Submenu Item 1", command=show_sub_menu_item1)
    setting_submenu.add_command(label="Submenu Item 2", command=show_sub_menu_item2)
    file_menu.add_cascade(label="Settings", menu=setting_submenu)
    file_menu.add_command(label= 'Exit', command= window.destroy)
    

    #settings_menu = Menu(menubar, tearoff=0)
    
    menubar.add_cascade(label = "File", menu = file_menu)
  
    sub_menu = Menu(file_menu, tearoff = 0)




   
    
    
    players = ["x", "o"]
    player = random.choice(players)
    buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    label_Title = Label(text = "Tic Tac Toe", font=('Helvetica bold', 26))
    label_Title.pack(side = "top")

    label = Label(text = "Player " + player + " turn")
    label.pack(side = "top")

    playerXWins = Label(text = "Player " + players[0] + " wins: " + str(xPlayerWins))
    playerXWins.place(x = 50, y = 100)
    playerYWins = Label(text = "Player " + players[1] + " wins: " + str(yPlayerWins))
    playerYWins.place(x = 50, y = 130)



    reset_button = Button(text = "Restart", command = new_game)
    reset_button.place(x = 50, y = 400)
    

    frame = Frame(window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", width=5, height=2,
                                        command= lambda row=row, column=column: next_turn(row,column))
            buttons[row][column].grid(row=row,column=column)
    window.mainloop()



if __name__ == "__main__":
    create3x3board()