import tkinter
import customtkinter
from tkinter import filedialog

def new():
    global file, file_rw

    file = filedialog.asksaveasfilename(initialdir="D:\(0001) Personal\Warden Park\Year 11\Computer Science\Word Processor - Text Document Revision GCSE Computer Science\Word Processor - Text Document Revision GCSE Computer Science", title = "Create Text File", filetypes = (("Text File", "*.txt"), ))
    file = file + ".txt"    
    root.title(file)
    file_rw = open(file, "w")

    file_rw.close()

def open_file():
    global file, file_rw

    file = filedialog.askopenfilename(initialdir="D:\(0001) Personal\Warden Park\Year 11\Computer Science\Word Processor - Text Document Revision GCSE Computer Science\Word Processor - Text Document Revision GCSE Computer Science", title = "Open Text File", filetypes = (("Text Files", "*.txt"), ))
    file_rw = open(file, "r+")

    text = file_rw.read()

    text_box.delete("0.0", "end")
    text_box.insert("end", text = text)

    file_rw.close()

def save():
    global file, file_rw

    if file != "":
        file_rw = open(file, "w+")

        file_rw.writelines(text_box.get("0.0", "end"))

        file_rw.close()
    else:
        new()

        file_rw = open(file, "r+")

        file_rw.writelines(text_box.get("0.0", "end"))

        file_rw.close()

file = ""

root = customtkinter.CTk()
root.geometry("750x750")    
root.title("No File Open")

customtkinter.set_appearance_mode("dark")

frame = customtkinter.CTkFrame(root)

frame.rowconfigure(0, weight = 1, minsize = 30)
frame.rowconfigure(1, weight = 10000)

frame.columnconfigure(0, weight = 1, minsize = 40)
frame.columnconfigure(1, weight = 1, minsize = 40)
frame.columnconfigure(2, weight = 1, minsize = 40)
frame.columnconfigure(3, weight = 1000000)

new_file_button = customtkinter.CTkButton(frame, text = "New File", command = new)
new_file_button.grid(row = 0, column = 0, sticky = "news", padx = 1, pady = 2)

open_file_button = customtkinter.CTkButton(frame, text = "Open File", command = open_file)
open_file_button.grid(row = 0, column = 1, sticky = "news", padx = 1, pady = 2)

save_file_button = customtkinter.CTkButton(frame, text = "Save", command = save)
save_file_button.grid(row = 0, column = 2, sticky = "news", padx = 1, pady = 2)

text_box = customtkinter.CTkTextbox(frame, wrap = "word", width = 750, corner_radius = 0)
text_box.grid(row = 1, column = 0, columnspan = 4, sticky = "nsew")

frame.pack(anchor = "center", expand = True, fill = "both")
root.mainloop()

file.writelines(text)
