from tkinter import *
import random

back_color = "#021526"
my_line_color = "#6EACDA"
action_color = "#E2E2B6"
turn_1 = "X"
turn_2 = "0"


board = [[7, 7, 7],
         [7, 7, 7],
         [7, 7, 7]]


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

game_step=int(1)
def button_press(house_num,):  # total game_step = 9

    global game_step

    if int(house_num) == 1:
        print(game_step)
        bu_text = str(do_process(game_step))
        buttom1.config(text=bu_text, bg=action_color,state="disabled")
        buttom1.update()
        board[0][0]=bu_text
    elif int(house_num) == 2:
        print(game_step)
        bu_text= str(do_process(game_step))
        buttom2.config(text=bu_text, bg=action_color,state="disabled")
        buttom2.update()
        board[0][1]=bu_text
    elif int(house_num) == 3:
        print(game_step)
        bu_text= str(do_process(game_step))
        buttom3.config(text=bu_text, bg=action_color,state="disabled")
        buttom3.update()
        board[0][2]=bu_text
    elif int(house_num) == 4:
        print(game_step)
        bu_text= str(do_process(game_step))
        buttom4.config(text=bu_text, bg=action_color,state="disabled")
        buttom4.update()
        board[1][0]=bu_text
    elif int(house_num) == 5:
        print(game_step)
        bu_text= str(do_process(game_step))
        buttom5.config(text=bu_text, bg=action_color,state="disabled")
        buttom5.update()
        board[1][1]=bu_text
    elif int(house_num) == 6:
        print(game_step)
        bu_text= str(do_process(game_step))
        buttom6.config(text=bu_text, bg=action_color,state="disabled")
        buttom6.update()
        board[1][2]=bu_text
    elif int(house_num) == 7:
        print(game_step)
        bu_text= str(do_process(game_step))
        buttom7.config(text=bu_text, bg=action_color,state="disabled")
        buttom7.update()
        board[2][0]=bu_text
    elif int(house_num) == 8:
        print(game_step)
        bu_text= str(do_process(game_step))
        buttom8.config(text=bu_text, bg=action_color,state="disabled")
        buttom8.update()
        board[2][1]=bu_text
    elif int(house_num) == 9:
        print(game_step)
        bu_text= str(do_process(game_step))
        buttom9.config(text=bu_text, bg=action_color,state="disabled")
        buttom9.update()
        board[2][2]=bu_text


    game_step= game_step+1
    for i in board:
        print(i)



window = Tk()

window.title('Tic Tac Toe')
window.minsize(584, 700)

window.config(bg=back_color)

buttom1 = Button(text=" ", width=25, height=10, bg=my_line_color, command=lambda: button_press(1))
buttom1.place(x=11, y=11)
buttom2 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(2))
buttom2.place(x=200, y=11)
buttom3 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(3))
buttom3.place(x=389, y=11)

buttom4 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(4))
buttom4.place(x=11, y=177)
buttom5 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(5))
buttom5.place(x=200, y=177)
buttom6 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(6))
buttom6.place(x=389, y=177)

buttom7 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(7))
buttom7.place(x=11, y=345)
buttom8 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(8))
buttom8.place(x=200, y=345)
buttom9 = Button(text="", width=25, height=10, bg=my_line_color, command=lambda: button_press(9))
buttom9.place(x=389, y=345)
canvas = Canvas(window, width=557, height=60, bg=my_line_color)

canvas.create_text(275, 30, text=f"{turn_1}'s turn", fill="black", font=12)
canvas.place(x=11, y=520)
window.mainloop()
