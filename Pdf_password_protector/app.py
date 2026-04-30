import pikepdf
import tkinter as tk
from tkinter import filedialog
import os
# create main window
root = tk.Tk()
root.title("pdf protector")
root.geometry("400x250")

selected_file = None # store file path

# label for file select or not 
label = tk.Label(root, text="no file selected yet:")
label.pack(pady=10, padx=10)

# function to open file dialog

def select_file():
    global selected_file
    file_path = filedialog.askopenfilename()
    
    if file_path:
        selected_file = file_path
        file_name = os.path.basename(file_path)
        label.config(text=f"Selected:{file_name}")
        btn2.config(state="normal") # enable second button
        password_label.pack(pady=5)
        password_entry.pack(pady=5)
        btn2.pack(pady=10)
# function for process file (next step)

def submit_pass():
    password = password_entry.get()
    if len(password) != 8:
        label.config(text="password must be 8 char")
        return
    try:
        pdf = pikepdf.open(selected_file)

        # output file name
        output_file = selected_file.replace(".pdf", "encry.pdf")
        pdf.save(
            output_file,
            encryption=pikepdf.Encryption(
                user=password,
                owner=password,
                R=4
            )
        )
        label.config(text="pdf protected susccessfully ")
        print("Saved as: ", output_file)
    except Exception as e:
        label.config(text="Error proeceessing wit this file")
        print(e)
# button to trigger file selection
btn1 = tk.Button(root, text="Choose file", command=select_file)
btn1.pack(pady=10)


btn2 = tk.Button(root, text="Submit", command=submit_pass, state="disabled")
btn2.pack(pady=10)
# hidden widgets
password_label = tk.Label(root, text="Enter pass")
password_entry = tk.Entry(root, show="*")
btn3 = tk.Button(root,text="Submit", command=submit_pass)
#run the win function
root.mainloop()


