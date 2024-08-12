import linecache
from tkinter import *
import random
import time

flag=int(1)
flag1=int(1)
back_color = "#021526"
my_line_color = "#6EACDA"
action_color = "#E2E2B6"
turn_1 = "X"
turn_2 = "0"
game_step = int(1)

board = [[7, 7, 7],
         [7, 7, 7],
         [7, 7, 7]]


def reset_game():
    global game_step
    for i in range(3):
        for j in range(3):
            board[i][j] = int(7)
    flag=int(0)
    time.sleep(1)
    flag0=int(1)
    game_step = int(1)
    window.destroy()
    print(game_step)





def check_win():
    canvas1=Canvas(window, height=50, width=400, bg=back_color)

    # We check the row for each player's win
    if board[0][0] == board[0][1] == board[0][2] != 7 or board[0][0] == board[0][1] == board[0][2] != 7:
        canvas1.create_text(205, 25, text=f"Game over\nPlayer {board[0][1]} win", fill="white", font=12)
        canvas1.place(x=90, y=250)
        print("Game Over")
        time.sleep(2)
        canvas1.delete()
    elif board[1][0] == board[1][1] == board[1][2] != 7 or board[1][0] == board[1][1] == board[1][2] != 7:
        canvas1.create_text(205, 25, text=f"Game over\nPlayer {board[1][1]} win", fill="white", font=12)
        canvas1.place(x=90, y=250)
        print("Game Over")
    elif board[2][0] == board[2][1] == board[2][2] != 7 or board[2][0] == board[2][1] == board[2][2] != 7:
        canvas1.create_text(205, 25, text=f"Game over\nPlayer {board[2][1]} win", fill="white", font=12)
        canvas1.place(x=90, y=250)
        print("Game Over")


        # We check the column for each player's win
    elif board[0][0] == board[1][0] == board[2][0] != 7 or board[0][0] == board[1][0] == board[2][0] != 7:
        canvas1.create_text(205, 25, text=f"Game over\nPlayer {board[1][0]} win", fill="white", font=12)
        canvas1.place(x=90, y=250)
        print("Game Over")
    elif board[0][1] == board[1][1] == board[2][1] != 7 or board[0][1] == board[1][1] == board[2][1] != 7:
        canvas1.create_text(205, 25, text=f"Game over\nPlayer {board[1][1]} win", fill="white", font=12)
        canvas1.place(x=90, y=250)
        print("Game Over")
    elif board[0][2] == board[1][2] == board[2][2] != 7 or board[0][2] == board[1][2] == board[2][2] != 7:
        canvas1.create_text(205, 25, text=f"Game over\nPlayer {board[1][2]} win", fill="white", font=12)
        canvas1.place(x=90, y=250)
        print("Game Over")

    # we check primary diagonal for each player win
    elif board[0][0] == board[1][1] == board[2][2] != 7 or board[0][0] == board[1][1] == board[2][2] != 7:
        canvas1.create_text(205, 25, text=f"Game over\nPlayer {board[1][1]} win", fill="white", font=12)
        canvas1.place(x=90, y=250)
        print("Game Over")

    # we check secondary diagonal for each player win
    elif board[2][0] == board[1][1] == board[0][2] != 7 or board[2][0] == board[1][1] == board[2][2] != 7:
        canvas1.create_text(205, 25, text=f"Game over\nPlayer {board[1][1]} win", fill="white", font=12)
        canvas1.place(x=90, y=250)
        print("Game Over")


def do_process(step1):
    if int(step1) % 2 == 0:
        button_text = str(turn_2)
        game_turn = str(turn_1)
        canvas.delete("all")
        canvas.create_text(275, 30, text=f"{game_turn}'s turn", fill="black", font=12)
        return button_text
    elif int(step1) % 2 != 0:
        button_text = str(turn_1)
        game_turn = str(turn_2)
        canvas.delete("all")
        canvas.create_text(275, 30, text=f"{game_turn}'s turn", fill="black", font=12)
        return button_text


def button_press(house_num, ):  # total game_step = 9

    global game_step

    if int(house_num) == 1:
        print(game_step)
        bu_text = str(do_process(game_step))
        button1.config(text=bu_text, bg=action_color, state="disabled")
        button1.update()
        board[0][0] = bu_text
        check_win()
    elif int(house_num) == 2:
        print(game_step)
        bu_text = str(do_process(game_step))
        button2.config(text=bu_text, bg=action_color, state="disabled")
        button2.update()
        board[0][1] = bu_text
        check_win()
    elif int(house_num) == 3:
        print(game_step)
        bu_text = str(do_process(game_step))
        button3.config(text=bu_text, bg=action_color, state="disabled")
        button3.update()
        board[0][2] = bu_text
        check_win()
    elif int(house_num) == 4:
        print(game_step)
        bu_text = str(do_process(game_step))
        button4.config(text=bu_text, bg=action_color, state="disabled")
        button4.update()
        board[1][0] = bu_text
        check_win()
    elif int(house_num) == 5:
        print(game_step)
        bu_text = str(do_process(game_step))
        button5.config(text=bu_text, bg=action_color, state="disabled")
        button5.update()
        board[1][1] = bu_text
        check_win()
    elif int(house_num) == 6:
        print(game_step)
        bu_text = str(do_process(game_step))
        button6.config(text=bu_text, bg=action_color, state="disabled")
        button6.update()
        board[1][2] = bu_text
        check_win()
    elif int(house_num) == 7:
        print(game_step)
        bu_text = str(do_process(game_step))
        button7.config(text=bu_text, bg=action_color, state="disabled")
        button7.update()
        board[2][0] = bu_text
        check_win()
    elif int(house_num) == 8:
        print(game_step)
        bu_text = str(do_process(game_step))
        button8.config(text=bu_text, bg=action_color, state="disabled")
        button8.update()
        board[2][1] = bu_text
        check_win()
    elif int(house_num) == 9:
        print(game_step)
        bu_text = str(do_process(game_step))
        button9.config(text=bu_text, bg=action_color, state="disabled")
        button9.update()
        board[2][2] = bu_text
        check_win()

    game_step = game_step + 1
    for i in board:
        print(i)

while(flag1):
    while(flag):
        window = Tk()

        window.title('Tic Tac Toe')
        window.minsize(584, 700)

        window.config(bg=back_color)

        button1 = Button(text=" ", width=25, height=10, bg=my_line_color, command=lambda: button_press(1))
        button1.place(x=11, y=11)
        button2 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(2))
        button2.place(x=200, y=11)
        button3 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(3))
        button3.place(x=389, y=11)

        button4 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(4))
        button4.place(x=11, y=177)
        button5 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(5))
        button5.place(x=200, y=177)
        button6 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(6))
        button6.place(x=389, y=177)

        button7 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(7))
        button7.place(x=11, y=345)
        button8 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(8))
        button8.place(x=200, y=345)
        button9 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(9))
        button9.place(x=389, y=345)
        canvas = Canvas(window, width=557, height=60, bg=my_line_color)

        canvas.create_text(275, 30, text=f"{turn_1}'s turn", fill="black", font=12)
        canvas.place(x=11, y=520)
        button_reset = Button(text="Reset Game", width=50, height=3, bg=my_line_color, font=20,command=reset_game)
        button_reset.place(x=12, y=590)

        window.mainloop()
