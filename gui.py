# import tkinter for the GUI
from tkinter import *

# Make a default window using tkinter

window = Tk()
window.title("Chatbot")
window.geometry("400x500")
window.resizable(0,0)
window.iconbitmap(r"chatbot_icon22.ico")

canvas = Canvas(window, height=500,width=400)
canvas.pack()

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
i = 20

def addchatbot_image():
    global i
    image = Label(window, image=chatbot_image)
    if i<350:
        canvas.create_window(20, i, window=image)
        #round_rectangle(90, i, 250, 50+i, r=20, outline="#64B5F6", fill="white")
    i += 70

def add_user_image():
    global i
    image = Label(window, image=user_image)
    if i<350:
        canvas.create_window(370, i+15, window=image)
        j = len(input_box.get("1.0", END))
        k = 30
        if j>300:
            k *= (j/300)
            j = 300
        elif j<50:
            j = 50
        #round_rectangle(310-j, i, 310, i+k, r=20, outline="#64B5F6", fill = "white")
        text = Label(window, text=input_box.get("1.0", END), justify = RIGHT, pady=4, wraplength=300)
        canvas.create_window(345-j, i+25, window=text)
    i += 70

def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return canvas.create_polygon(points, **kwargs, smooth=True)


# line above send button



# chatbot messages
def chatbot_message():
    add_user_image()

# send button image
send_image = PhotoImage(file="send.png")
send = Button(canvas, image= send_image, height=100, width =200, command = chatbot_message, borderwidth=0)
send.place(x=200, y= 400)

# use chatbot functions to display the responses in GUI


window.mainloop()