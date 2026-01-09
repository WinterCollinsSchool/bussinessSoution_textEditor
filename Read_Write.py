import customtkinter

app=customtkinter.CTk()
app.title("Simple CTkinter App")

app.geometry("300x150")

text_box = customtkinter.CTkTextbox(app)

text_box.pack()