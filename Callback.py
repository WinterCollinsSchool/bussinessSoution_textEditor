import customtkinter
import random

root = customtkinter.CTk()
root.title("Enter Title Here")

root.geometry("300x150")

def callback1():
	label1.configure(text="Updated 1!")
def callback2():
	label2.configure(text="Updated 2!")
def callback3():
	label3.configure(text="Updated 3!")
def random():
	

label1=customtkinter.CTkLabel(root, text="Lable 1!")
label2=customtkinter.CTkLabel(root, text="Lable 2!")
label3=customtkinter.CTkLabel(root, text="Lable 3!")

button1=customtkinter.CTkButton(root, text="Button 1!",command=callback1)
button2=customtkinter.CTkButton(root, text="Button 2!",command=callback2)
button3=customtkinter.CTkButton(root, text="Button 3!",command=callback3)



random_button=customtkinter.CTkButton(root, text="Random Button!",command=random())


button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
button3.grid(row=2,column=0)

label1.grid(row=0,column=3)
label2.grid(row=1,column=3)
label3.grid(row=2,column=3)

root.mainloop()