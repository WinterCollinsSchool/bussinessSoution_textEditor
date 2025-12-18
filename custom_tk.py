import customtkinter

root=customtkinter.CTk()
root.title("Word Prosesser")

root.geometry("300x150")

def save_as():
	new_file_name=input("Save as:")
	clean_file_name=new_file_name+".txt"
	text=text_box.get("1.0", "end-1c")
	f = open(clean_file_name,"x")
	with open(clean_file_name, "w") as f:
		f.write(text)
	with open(clean_file_name) as f:
		print(f.read())

save=customtkinter.CTkButton(root,text="Save",command = lambda:save_as())
label = customtkinter.CTkLabel(root, text="Write your notes here!")
text_box = customtkinter.CTkTextbox(root,height=15,width=50)

label.grid(row=0,column=0,pady=5,padx=10)
text_box.grid(row=1,column=0, columnspan=2,padx=5)
save.grid(row=0,column=1)

root.mainloop()