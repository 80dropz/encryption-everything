from tkinter import *
import customtkinter
from customtkinter import filedialog
import keyboard
import os.path
import random
import time
import pyperclip



keygenereated = int(0)
keygenereatedalready = int(1)
keygenereatedcheck = False
filetxtbool = False




def center_window(window, width, height):
    # Get the screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position of the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window position and size
    window.geometry(f"{width}x{height}+{x}+{y}")




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
    global keygenereated


    cap = customtkinter.CTkToplevel()
    cap.title("Click to copy")
    width = 300
    height = 200
    customtkinter.set_appearance_mode("Dark")
    center_window(cap, width, height)


    capwindow = customtkinter.CTkLabel(master=cap, text="Click to copy your key", font=("Arial", 20), text_color="green")
    capwindow.place(relx=.5 , rely=.2, anchor="center")


    copybtn = customtkinter.CTkButton(master=cap, text="Click me", command=copykey)
    copybtn.place(relx=.5 , rely=.5, anchor="center")
    key2 = random.getrandbits(128)
    key1 = random.getrandbits(128)
    key = key1 + key2
    key1lbl.configure(text=key, font=("roboto", 12))
    writelog = open("log.txt", "w")
    writelog.write( f"Keep me safe: {key}")
    print(key)
    writelog.close()
    keygenereated = True

    cap.mainloop()

def copykey():
    pyperclip.copy(key)
def encrypt():
    keystr = str(key)
    if filetxtbool == True and keygenereated == True:
        encryptlbl.configure(text="Encrytion started", text_color="green")
        read = open(filename, "r")
        content = read.read()
        print(content)
        content1 = content.replace("a", keystr[-23:])
        content2 = content1.replace("b", keystr[-2:])
        content3 = content2.replace("c", keystr[-12:])
        content4 = content3.replace("d", keystr[-26:])
        content5 = content4.replace("e", keystr[-32:])
        content6 = content5.replace("f", keystr[-6:])
        content7 = content6.replace("g", keystr[-18:])
        content8 = content7.replace("h", keystr[-8:])
        content9 = content8.replace("i", keystr[-14:])
        content10 = content9.replace("j", keystr[-22:])
        content11 = content10.replace("k", keystr[-30:])
        content12 = content11.replace("l", keystr[-4:])
        content13 = content12.replace("m", keystr[-16:])
        content14 = content13.replace("n", keystr[-10:])
        content15 = content14.replace("o", keystr[-24:])
        content16 = content15.replace("p", keystr[-34:])
        content17 = content16.replace("q", keystr[-5:])
        content18 = content17.replace("r", keystr[-20:])
        content19 = content18.replace("s", keystr[-28:])
        content20 = content19.replace("t", keystr[-32:])
        content21 = content20.replace("u", keystr[-6:])
        content22 = content21.replace("v", keystr[-18:])
        content23 = content22.replace("w", keystr[-8:])
        content24 = content23.replace("x", keystr[-14:])
        content25 = content24.replace("y", keystr[-22:])
        content26 = content25.replace("z", keystr[-30:])
        writingtest = open("test.txt", "w")
        writingtest.write(content26)
        writingtest.close()


        print(content1)
    elif filetxtbool == True and keygenereated == False:
        encryptlbl.configure(text="Error You need to generate your key", text_color="red")
    elif filetxtbool == False and keygenereated == True:
        encryptlbl.configure(text="Error You dont have a file entered", text_color="red")


main=customtkinter.CTk()
main.geometry("400x400")
main.title("Dropz Encrypter")
customtkinter.set_appearance_mode("Dark")

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
