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

send = Button(text="Send", command = send_msg)
send.pack()




# use chatbot functions to display the responses in GUI


window.mainloop()