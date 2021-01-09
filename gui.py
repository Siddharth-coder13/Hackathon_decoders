# import tkinter for the GUI
from tkinter import *

# Make a default window using tkinter

window = Tk()
window.title("Chatbot")
window.geometry("400x500")

# Add widgets in the window

#write commands to send message
def send_msg() :
    print("message")

# send button image
send_image = PhotoImage(file="send.png")

send = Button(window, image= send_image, height=100, width =200, command = send_msg, borderwidth=0)
send.place(x=200, y= 400)

# line above send button
line = Canvas(window, height=420, width= 500)
line.create_line(0, 405, 400, 405, width=2,fill="#64B5F6")
line.pack()

# input box to get user input
input_box = Text(window, height=4, width= 25, highlightthickness=2)
input_box.config(highlightbackground="#64B5F6", highlightcolor= "#64B5F6")
input_box.place(x=10, y = 420)


# use chatbot functions to display the responses in GUI


window.mainloop()