from tkinter import *

win = Tk()
win.title("Canvas X-Axis Line")

# Create the canvas
canvas = Canvas(win, width=500, height=500, bg="blue")
canvas.pack()

# Draw a line along the x-axis (horizontal line at y = 250)
# canvas.create_line(0,0,500,500, fill="blue", width=3)
# canvas.create_line(500,0,0,500, fill="blue", width=3)
# canvas.create_line(0,250,500,250, fill="blue", width=3)
# canvas.create_line(250,0,250,500, fill="blue", width=3)


# canvas.create_arc(50, 50, 150, 150, start=0, extent=180, fill="red", outline="black")

# canvas.create_oval(20,20,200,300,fill="red", width=3)

# coords=[20,20,50,50,40,100]

# canvas.create_polygon(coords, fill="red", outline="black")

file_1=PhotoImage(file="../download.png")

canvas.create_text(300, 300, text="Hello World", fill="white", font=("Arial", 20))

canvas.create_image(250, 250, image=file_1)


win.mainloop()
