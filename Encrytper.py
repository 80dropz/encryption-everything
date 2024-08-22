import tkinter
import customtkinter
from customtkinter import filedialog
import keyboard
import os.path
import random
import time
def bools():
    global keygenereatedcheck
    global keygenereated
    global filetxtbool
    global keygenereatedalready
    keygenereated = int(0)
    keygenereatedalready = int(1)
    keygenereatedcheck = False
    filetxtbool = False

with open('key.txt', encoding='utf8') as file_object:
    key = file_object.read()


def file():
    global filetxtbool
    global filename
    filename = filedialog.askopenfilename()
    if filename.endswith('.txt'):
        checking.configure(text="Text file click ecrypt button to encrypt")
        filetxtbool = True
    else: 
        checking.configure(text="File must end with txt")

def savekey():
    time.sleep(3)
    savethiskey.configure(text=" ")
def generatekey():
    global key
    key2 = random.getrandbits(128)
    key1 = random.getrandbits(128)
    key = key2 + key1
    key1lbl.configure(text=key1, font=("roboto", 12))
    key2lbl.configure(text=key2, font=("roboto", 12))
    savethiskey.configure(text=" SAVE THIS KEY ", text_color="Green", font=("Roboto", 24))
    savekey()
    

def encrypt():
    if filetxtbool == True and keygenereated == True:
        encryptlbl.configure(text="Encrytion started", text_color="green")
        read = open(filename, "r")
        print(read)
    elif filetxtbool == True and keygenereated == False:
        encryptlbl.configure(text="Error You need to generate your key", text_color="red")
    elif filetxtbool == False and keygenereated == True:
        encryptlbl.configure(text="Error You dont have a file entered", text_color="red")

main=tkinter.Tk()
main.geometry("400x400")
main.title("Dropz Encrypter")


header = customtkinter.CTkLabel(main, text="Dropz Encrypter", font=("Arial", 20))
header.place(relx=.5 , rely=.05, anchor="center")

txttoencrypt = customtkinter.CTkButton(master=main, text="file to encrypt", font=("Arial", 10), command=file)
txttoencrypt.place(relx=.5 , rely=.15, anchor="center")

keyentry = customtkinter.CTkButton(master=main, text="Generate Key", command=generatekey)
keyentry.place(relx=.5 , rely=.25, anchor="center")

Encrpytbtn = customtkinter.CTkButton(master=main, text="Encrypt", command=encrypt)
Encrpytbtn.place(relx=.5 , rely=.35, anchor="center")

key1lbl = customtkinter.CTkLabel(master=main, text=" ")
key1lbl.place(relx=.5 , rely=.45, anchor="center")

key2lbl = customtkinter.CTkLabel(master=main, text=" ")
key2lbl.place(relx=.5, rely=.53, anchor="center" )

checking = customtkinter.CTkLabel(master=main, text=" ")
checking.place(relx=.5, rely=.62, anchor="center")

encryptlbl = customtkinter.CTkLabel(master=main, text=" ")
encryptlbl.place(relx=.5, rely=.70, anchor="center")

savethiskey = customtkinter.CTkLabel(master=main, text=" ")
savethiskey.place(relx=.3, rely=.3, anchor="center")
main.mainloop()
