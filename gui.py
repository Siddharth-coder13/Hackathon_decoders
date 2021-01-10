# import tkinter for the GUI
from tkinter import *
import chatbot

# Make a default window using tkinter

window = Tk()
window.title("Chatbot")
window.geometry("400x500")
window.resizable(0,0)
window.iconbitmap(r"chatbot_icon22.ico")



canvas = Canvas(window, height=500,width=400)
canvas.pack()

# train the chatbot
chatbot.train()

# Add widgets in the window

#write commands to send message
def send_msg() :
    print("message")


# input box to get user input
input_box = Text(window, height=4, width= 25, highlightthickness=2)
input_box.config(highlightbackground="#64B5F6", highlightcolor= "#64B5F6")
input_box.place(x=10, y = 420)

# chatbot image
chatbot_image = PhotoImage(file="chatbot_icon.png")
user_image = PhotoImage(file="user.png")
i = 15

def addchatbot_image():
    global i
    image = Label(window, image=chatbot_image)
    if i<350:
        image.place(x=15, y=i)
        res = chatbot.response(input_box.get("1.0", END))
        bot_text = Label(window, anchor=W, text=res, wraplength=270, justify=LEFT)
        bot_text.place(x=75, y=i+21)
    i += 60

def add_user_image():
    global i
    image = Label(window, image=user_image)
    if i<350:
        canvas.create_window(350, i+15, window=image)
        j = len(input_box.get("1.0", END))
        if j<40:
            j = 40
            text = Label(window, text=input_box.get("1.0", END), justify = RIGHT, wraplength=270, anchor=E)
            canvas.create_window(300-j, i+20, window=text)
    i += 50

# line above send button


# chatbot messages
def chatbot_message():
    add_user_image()
    addchatbot_image()
    input_box.delete("1.0", END)

# send button image
send_image = PhotoImage(file="send.png")
send = Button(canvas, image= send_image, height=100, width =200, command = chatbot_message, borderwidth=0)
send.place(x=200, y= 400)



window.mainloop()