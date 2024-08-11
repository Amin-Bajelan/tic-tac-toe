from tkinter import *
import random

back_color = "#021526"
my_line_color = "#6EACDA"
action_color = "#E2E2B6"
turn = "X"


def insert_symbol1():
    buttom1.config(text=select)


def insert_symbol9():
    buttom9.config(text="X", bg=action_color, font=12)


window = Tk()

window.title('Tic Tac Toe')
window.minsize(584, 700)

window.config(bg=back_color)

buttom1 = Button(text="", width=25, height=10, bg=my_line_color)
buttom1.place(x=11, y=11)
buttom2 = Button(text="", width=25, height=10, bg=my_line_color)
buttom2.place(x=200, y=11)
buttom3 = Button(text="", width=25, height=10, bg=my_line_color)
buttom3.place(x=389, y=11)

buttom4 = Button(text="", width=25, height=10, bg=my_line_color)
buttom4.place(x=11, y=177)
buttom5 = Button(text="", width=25, height=10, bg=my_line_color)
buttom5.place(x=200, y=177)
buttom6 = Button(text="", width=25, height=10, bg=my_line_color)
buttom6.place(x=389, y=177)

buttom7 = Button(text="", width=25, height=10, bg=my_line_color)
buttom7.place(x=11, y=345)
buttom8 = Button(text="", width=25, height=10, bg=my_line_color)
buttom8.place(x=200, y=345)
buttom9 = Button(text="", width=25, height=10, bg=my_line_color, command=insert_symbol9)
buttom9.place(x=389, y=345)
canvas = Canvas(window,width= 557, height= 60, bg=my_line_color)

window.mainloop()
canvas.create_text(275, 30, text=f"{turn}'s turn", fill="black" ,font=12)
canvas.place(x=11, y=520)
