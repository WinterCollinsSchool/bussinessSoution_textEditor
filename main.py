import customtkinter

root = customtkinter.CTk()
root.title("Word Processor")

root.geometry("300x150")


def save_as():
    new_file_name = customtkinter.CTkInputDialog(text="Save as:", title="Save")
    clean_file_name = new_file_name.get_input() + ".txt"
    text = text_box.get("1.0", "end-1c")
    f = open(clean_file_name, "x")
    with open(clean_file_name, "w") as f:
        f.write(text)
    with open(clean_file_name) as f:
        print(f.read())
    root.destroy()

root.grid_columnconfigure(1, weight=1)
save = customtkinter.CTkButton(root, text="Save", command=lambda: save_as())
label = customtkinter.CTkLabel(root, text="Write your notes here!")
text_box = customtkinter.CTkTextbox(root, height=500, width=500)

label.grid(row=0, column=0, pady=5,sticky="w", padx=5)
text_box.grid(row=1, column=0, columnspan=2, padx=5,sticky="ews")
save.grid(row=0, column=1, padx=10, sticky="w")

root.mainloop()
