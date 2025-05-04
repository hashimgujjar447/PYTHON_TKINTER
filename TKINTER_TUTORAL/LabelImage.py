from tkinter import *

window=Tk()
window.geometry("400x300")
window.title("Label")


# photo=PhotoImage(file="../download.png")



# lb=Label(window,
#          image=photo,
#             text="Hello World",
#             font=("Arial", 20, "bold"),
#             compound="top",
            
#          )

# lb.place(x=50,y=50)


label_frame=LabelFrame(window,
              text="Python",
              font=("Arial", 20, "bold"),
            labelanchor="nw"

              )
label_frame.place(x=50,y=50,height=100,width=500)

label_frame.config(bd=5, relief="sunken")

lb=Label(window,
         text="Hello World",
         font=("Arial", 20, "bold"),
         bg="gray",
         relief="sunken",
         justify=LEFT,

)
lb.place(x=50,y=100)


window.mainloop()




