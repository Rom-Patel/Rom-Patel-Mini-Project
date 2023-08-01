from tkinter import *
from tkinter import Scale, colorchooser, filedialog, messagebox
import pyautogui

window = Tk()
window.state("zoomed")
window.title("Paint Application")

# variables
pen_color = "black"
eraser_color = "white"

# Canvas
canvas = Canvas(window, bg="white", bd=5, relief=GROOVE, height=800, width=1800)
canvas.place(x=0, y=100)

# Function
def canvas_color():
    global eraser_color
    color = colorchooser.askcolor()
    canvas.configure(bg=color[1])
    eraser_color = color[1]

def save():
    file_name = filedialog.asksaveasfilename(defaultextension=".jpg")
    x, y, width, height = canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_width(), canvas.winfo_height()
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(file_name)
    messagebox.showinfo("Paint Notification", "Image is Saved as " + str(file_name))

def eraser():
    global pen_color
    pen_color = eraser_color

def clear():
    canvas.delete("all")

def paint(event):
    x1, y1 = (event.x-2), (event.y-2)
    x2, y2 = (event.x+2), (event.y+2)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline=pen_color, width=pen_size.get())

canvas.bind("<B1-Motion>", paint)

def select_color(col):
    global pen_color
    pen_color = col

# Frame
color_frame = LabelFrame(window, text="Color", relief=RIDGE, bg="white", font=("arial", 15, "bold"))
color_frame.place(x=10, y=10, width=424, height=60)

tool_frame = LabelFrame(window, text="Tools", relief=RIDGE, bg="white", font=("arial", 15, "bold"))
tool_frame.place(x=450, y=10, width=365, height=60)  # Increased width

pen_size_frame = LabelFrame(window, text="Size", relief=RIDGE, bg="white", font=("arial", 15, "bold"))
pen_size_frame.place(x=850, y=10, width=224, height=70)  # Adjusted position

# Color
colors = ['#ff0000', '#ff4dd2', '#ffff33', '#000000', '#0066ff', '#660033', '#4dff4d', '#b300b3', '#00ffff', '#808080', '#99ffcc']

# Buttons
i = j = 0
for color in colors:
    Button(color_frame, bd=3, bg=color, relief=RIDGE, width=3, command=lambda col=color: select_color(col)).grid(row=j, column=i, padx=1)
    i += 1
    if i > 10:
        i = 0
        j += 1

# Tool Buttons
canvas_color_b1 = Button(tool_frame, text="Canvas", bd=4, bg="white", command=canvas_color, relief=RIDGE, width=8)
canvas_color_b1.grid(row=0, column=0, padx=2)

save_b2 = Button(tool_frame, text="Save", bd=4, bg="white", command=save, relief=RIDGE, width=8)
save_b2.grid(row=0, column=1, padx=2)

eraser_b3 = Button(tool_frame, text="Erase", bd=4, bg="white", command=eraser, relief=RIDGE, width=8)
eraser_b3.grid(row=0, column=2, padx=2)

clear_b4 = Button(tool_frame, text="Clear", bd=4, bg="white", command=clear, relief=RIDGE, width=8)  # Increased width
clear_b4.grid(row=0, column=3, padx=2)

# Pen and eraser size
pen_size = Scale(pen_size_frame, orient=HORIZONTAL, from_=0, to=50, length=170)
pen_size.set(1)
pen_size.grid(row=0, column=0)

window.mainloop()
