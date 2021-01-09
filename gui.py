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

send_image = PhotoImage(file="send.png")


send = Button(window, image= send_image, height=100, width =200, command = send_msg, borderwidth=0)
send.place(x=200, y= 400)

# use chatbot functions to display the responses in GUI


window.mainloop()