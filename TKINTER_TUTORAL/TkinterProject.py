# School markSheet
from tkinter import *
from tkinter.messagebox import askokcancel,showerror,showinfo


#------------------------------------------------------------

#Function to calculate total marks

    # Get the marks from the entry fields

def calculate_total_marks():
    try:
        marks = []

        name=std_name_var.get().strip()
        if name == "":
            showerror("Input Error", "Student name must be filled.")
            return
      


        for var in [sub1_marks, sub2_marks, sub3_marks, sub4_marks, sub5_marks]:
            val = var.get().strip()
            if val == "":
                showerror("Input Error", "All subject marks must be filled.")
                return
            num = float(val)
            if num < 0:
                showerror("Input Error", "Marks cannot be negative.")
                return
            marks.append(num)

        total = sum(marks)

        percentage = total / 5
        grade = ""
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "Fail"


        response=askokcancel("Knowledge Hub", f"Student Name :{name} \nTotal Marks: {total}\nPercentage: {percentage:.2f}%\nGrade: {grade}")

        if response:
            std_name_var.set("")
            sub1_marks.set("0.0")
            sub2_marks.set("0.0")
            sub3_marks.set("0.0")
            sub4_marks.set("0.0")
            sub5_marks.set("0.0")
            std_name_entry.focus_set()
            with open("marks.txt","a") as file:
                file.write(f"Student Name: {name}\n")
                file.write(f"Total Marks: {total}\n")
                file.write(f"Percentage: {percentage:.2f}%\n")
                file.write(f"Grade: {grade}\n")
                file.write("-" * 30 + "\n")
                file.write("\n")
            file.close()
            showinfo("Marks Saved", "Marks have been saved successfully.")
        

    except ValueError:
        showerror("Input Error", "Please enter valid numeric values for all marks.")


  



win=Tk() # Start
win.config(bg="yellow")
win.title("School MarkSheet")

win.iconbitmap(r"C:\Users\kashi\Downloads\school.ico") # Icon

win.resizable(0,0) # Disable resizing

# Setting screen in middle

width=win.winfo_screenwidth()
height=win.winfo_screenheight()

x=int((width/2)-(500/2))
y=int((height/2)-(500/2))

win.geometry(f"500x500+{x}+{y}") # Set window size and position

#------------------------------------------------------------


school_name=Label(win,text="Knowledge Hub ",font=("Arial",30,"bold"),bg="yellow",fg="black")

school_name.place(x=25,y=20,height=60,width=450) # Set position of label


#------------------------------------------------------------

# variable for student name
std_name_var=StringVar(value="") # Default value is empty string

std_name=Label(win,text="Student Name",font=("Arial",15,"bold"),fg="black")
std_name.place(x=20,y=100,height=30,width=150) # Set position of label

std_name_entry=Entry(win,font=("Arial",15,"bold"),bg="white",fg="black",textvariable=std_name_var)
std_name_entry.place(x=180,y=100,height=30,width=300) # Set position of entry

#------------------------------------------------------------

sbj_name=Label(win,text="Subject Name",font=("Arial",20,"bold"),fg="black",bg="yellow")

sbj_name.place(x=50,y=150,height=30,width=400) # Set position of label



#------------------------------------------------------------



# all subject variables
sub1_marks=StringVar(value="0.0") # Default value is empty string
sub2_marks=StringVar(value="0.0") # Default value is empty string
sub3_marks=StringVar(value="0.0") # Default value is empty string
sub4_marks=StringVar(value="0.0") # Default value is empty string
sub5_marks=StringVar(value="0.0") # Default value is empty string    

"---------------------------------------------------------------"


#Subject names
sub1=Label(win,text="English",font=("Arial",15,"bold"),fg="black")
sub1.place(x=20,y=200,height=30,width=150) # Set position of label

sub1_entry=Entry(win,font=("Arial",15,"bold"),bg="white",fg="black",textvariable=sub1_marks)
sub1_entry.place(x=180,y=200,height=30,width=300) # Set position of entry


sub2=Label(win,text="Urdu",font=("Arial",15,"bold"),fg="black")
sub2.place(x=20,y=250,height=30,width=150) # Set position of label

sub2_entry=Entry(win,font=("Arial",15,"bold"),bg="white",fg="black",textvariable=sub2_marks)
sub2_entry.place(x=180,y=250,height=30,width=300) # Set position of entry

sub3=Label(win,text="Science",font=("Arial",15,"bold"),fg="black")
sub3.place(x=20,y=300,height=30,width=150) # Set position of label

sub3_entry=Entry(win,font=("Arial",15,"bold"),bg="white",fg="black", textvariable=sub3_marks)
sub3_entry.place(x=180,y=300,height=30,width=300) # Set position of entry

sub4=Label(win,text="Math",font=("Arial",15,"bold"),fg="black")
sub4.place(x=20,y=350,height=30,width=150) # Set position of label

sub4_entry=Entry(win,font=("Arial",15,"bold"),bg="white",fg="black",textvariable=sub4_marks)
sub4_entry.place(x=180,y=350,height=30,width=300) # Set position of entry


sub5=Label(win,text="SST",font=("Arial",15,"bold"),fg="black")
sub5.place(x=20,y=400,height=30,width=150) # Set position of label

sub5_entry=Entry(win,font=("Arial",15,"bold"),bg="white",fg="black",textvariable=sub5_marks)
sub5_entry.place(x=180,y=400,height=30,width=300) # Set position of entry


#------------------------------------------------------------
# Button to calculate total marks


btn=Button(win,text="Calculate Total Marks",font=("Arial",15,"bold"),activebackground="black",activeforeground="white",cursor="hand2",relief="ridge",command=calculate_total_marks)
btn.place(x=20,y=450,height=30,width=460) # Set position of button





win.mainloop()

