from cgitb import text
from ctypes import alignment
from tkinter import messagebox
from turtle import left
import mysql.connector
from tkinter import*

class AddDailyHelp:
    def __init__(self,root):
        self.root=root 
        self.root.title("Daily Help")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="light blue")
        self.root.focus_force() 
        title=Label(self.root,text="Add Daily Help",font=("goudy old style",20,"bold"),bg="black",fg="white").place(x=10,y=15,width=1180,height=35)
        
        self.var_WorkerName=StringVar()
        self.var_WorkerContact=StringVar()
        self.var_WorkerSalary=StringVar()

        lbl_DailyName=Label(self.root,text = "Name",font=("goudy old style",15,"bold"),bg="light blue").place(x=10,y=60)
        lbl_DailyContact=Label(self.root,text = "Contact Number",font=("goudy old style",15,"bold"),bg="light blue").place(x=10,y=100)
        lbl_DailySalary=Label(self.root,text = "Salary",font=("goudy old style",15,"bold"),bg="light blue").place(x=10,y=140)
        
        txt_ResidentName=Entry(self.root,textvariable=self.var_WorkerName,font=("goudy old style",15),bg="light blue").place(x=200,y=60)
        txt_Contact=Entry(self.root,textvariable=self.var_WorkerContact,font=("goudy old style",15),bg="light blue").place(x=200,y=100)
        txt_Salary=Entry(self.root,textvariable=self.var_WorkerSalary,font=("goudy old style",15),bg="light blue").place(x=200,y=140)
        
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add).place(x=230,y=270,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.clear).place(x=350,y=270,width=110,height=40)

       
    def add(self):
        con=mysql.connector.connect(host="localhost",user="root",password="dhanush@sql489",database="AMS")
        cur=con.cursor()
        cur.execute("insert into DailyHelp (Name,Contact,Salary) values (%s,%s,%s)",(
        self.var_WorkerName.get(),
        self.var_WorkerContact.get(),
        self.var_WorkerSalary.get()
        ))
        con.commit()
        messagebox.showinfo("Success"," Details Added Successfully") 

    def clear(self):
        self.var_WorkerName.set("")
        self.var_WorkerContact.set("")
        self.var_WorkerSalary.set("")
        

if __name__=="__main__":
    root=Tk()
    obj=AddDailyHelp(root)
    root.mainloop()

