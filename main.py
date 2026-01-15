import customtkinter

root = customtkinter.CTk()
root.title("Word Processor")

root.geometry("300x150")


def load_from():
    old_file_name = customtkinter.CTkInputDialog(text="What file?", title="Load")
    clean_old_file_name = old_file_name.get_input() + ".txt"
    with open(clean_old_file_name) as f:
        text_box.insert("0.0", f.read())

def save_as():
    new_file_name = customtkinter.CTkInputDialog(text="Save as:", title="Save")
    clean_new_file_name = new_file_name.get_input() + ".txt"
    text = text_box.get("1.0", "end-1c")
    with open("notes/"+clean_new_file_name, "w") as f:
        f.write(text)
    with open(clean_new_file_name) as f:
        print(f.read())
    root.destroy()

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(1, weight=1)

save_asb = customtkinter.CTkButton(root, text="Save", command=lambda: save_as())
label = customtkinter.CTkLabel(root, text="Write your notes here!")
text_box = customtkinter.CTkTextbox(root, height=500, width=500)
load = customtkinter.CTkButton(root,text="Load",command=lambda:load_from())

label.grid(row=0, column=0, pady=5,sticky="w", padx=5)
text_box.grid(row=1, column=0, columnspan=3, padx=5,sticky="news")
save_asb.grid(row=0, column=1, padx=10, sticky="we")
load.grid(row=0,column=2,padx=10,sticky="w")

root.mainloop()
