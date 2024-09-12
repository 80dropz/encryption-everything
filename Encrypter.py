import cryptography
from cryptography.fernet import Fernet
import customtkinter
from customtkinter import filedialog
import tkinter

key = Fernet.generate_key()
print(key)
k = Fernet(key)

def string_changed(*args):
    global string
    string = encryptentry.get()
    currenttext = f" current text: {string}"
    print(currenttext)
    lbltoencrypt.configure(text=string)

def encrypt():
    encstring = k.encrypt(string.encode())
    encstringfile = str(encstring)
    with open("encrypted.txt", "w") as f:
        f.write(encstringfile + "\n")
        f.write(f"Key to unencrypt: {key}")
mainwindow = customtkinter.CTk()
mainwindow.geometry("500x500")
mainwindow.title("An attempted encryption")


header = customtkinter.CTkLabel(master=mainwindow, text="An attempted encryption", font=("Arial", 20))
header.place(relx=.5, rely=.05, anchor="center")
subheader = customtkinter.CTkLabel(master=mainwindow, text="By: @80dropz", font=("Arial", 14))
subheader.place(relx=.5, rely=.1, anchor="center")

encryptbtn = customtkinter.CTkButton(master=mainwindow, text="Encrypt", command=encrypt)
encryptbtn.place(relx=.5, rely=.5, anchor="center")

encvar = customtkinter.StringVar()
encryptentry = customtkinter.CTkEntry(mainwindow, placeholder_text="Enter string to encrypt", width=150, height=50, textvariable=encvar)
encryptentry.place(relx=.5, rely=.6, anchor="center")
encvar.trace_add("write", string_changed)

lbltoencrypt = customtkinter.CTkLabel(master=mainwindow, text="Enter string to encrypt")
lbltoencrypt.place(relx=.5, rely=.8, anchor="center")

errorlbl = customtkinter.CTkLabel(master=mainwindow, text=" ", text_color="red")
errorlbl.place(relx=.5, rely=.7, anchor="center")
mainwindow.mainloop()
