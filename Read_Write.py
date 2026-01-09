import customtkinter

app=customtkinter.CTk()
app.title("Simple CTkinter App")

app.geometry("300x150")

text_box = customtkinter.CTkTextbox(app)
write=customtkinter.CTkButton(app,text='Write To File')
read=customtkinter.CTkButton(app,text='Read From File')

text_box.pack()
write.pack()
read.pack()