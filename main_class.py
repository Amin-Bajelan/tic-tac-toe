from tkinter import *
import random

back_color = "#021526"
my_line_color = "#6EACDA"
action_color = "#E2E2B6"

window = Tk()
window.geometry('500x500')
window.title('Tic Tac Toe')
# window.config(bg=back_color)
canvas1 = Canvas(window, width=500, height=500, background=back_color, highlightthickness=0)
canvas1.create_line(80, 190, 400, 190, fill=my_line_color, width=7)  #create for x line
canvas1.create_line(80, 290, 400, 290, fill=my_line_color, width=7)

canvas1.create_line(190, 100, 190, 400, fill=my_line_color, width=7)  #create for y line
canvas1.create_line(290, 100, 290, 400, fill=my_line_color, width=7)

place1 = [135, 155]
place2 = [240, 155]
place3 = [345, 155]
place4 = [135, 255]
place5 = [240, 255]
place6 = [345, 255]
place7 = [135, 360]
place8 = [240, 360]
place9 = [345, 360]

player_turn = random.randint(1, 2)
if player_turn == 1:
    print("First player is: *")
else:
    print("Second player is: |")


for i in range(1,10):

    print(i)


canvas1.place(x=0, y=0)

window.mainloop()
