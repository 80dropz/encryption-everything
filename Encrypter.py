import time 
from tkinter import *
import customtkinter
from customtkinter import filedialog
import random
import os

keygenerated = False
filelocationcheck = False
logexistscheck = False
plusoneonlog = False
foundinlog = False
oneclickgen = False

    





def dontuseprevious():
    logexists.destroy()



def useprevious():
    global keygenerated
    global foundinlog
    foundinlog = not False
    keygenerated = not False
    logexists.destroy()



if os.path.exists('logfile'):
    logexistscheck = not False
    logexists=customtkinter.CTk()
    logexists.title("Logfile check")
    logexists.geometry("300x200")

    header=customtkinter.CTkLabel(logexists, text="Previous Logfile found")
    header.place(relx=.5, rely=.2)

    subheader=customtkinter.CTkLabel(logexists, text="Do you want to use those keys?")
    subheader.place(relx=.5, rely=.27, anchor="center")

    yes = customtkinter.CTkButton(logexists, text="Yes use previous key's", fg_color="green", width=30, height=25, command=useprevious)
    yes.place(relx=.25, rely=.6, anchor="center")

    no = customtkinter.CTkButton(logexists, text="No generate new key's", fg_color="red", width=30, height=25, command=dontuseprevious)
    no.place(relx=.75, rely=.6, anchor="center")

    logexists.mainloop()
    

def filename():
    global flr
    global filelocationcheck
    filelocation = filedialog.askopenfilename()
    if filelocation.endswith(".txt"):
        flr = open(filelocation, "r")
        filelocationcheck = not False
        filelbl.configure(text="File is ready", text_color="green")
    else: 
        locationerror = customtkinter.CTk()
        locationerror.geometry("150x100")
        locationerror.title("Cannot find file")

        error = customtkinter.CTkLabel(master=locationerror, text="File must end with txt", text_color="red")
        error.place(relx=.5, rely=.5, anchor="center")

        locationerror.mainloop()
def encrypt():
    if keygenerated == True:
        if filelocationcheck == True:
            encryptionstarted.configure(text="Starting Encryption", text_color="green")
            flr2 = flr.read()
            flr2str = str(flr2)
            logfile = open("logfile", "r")
            line1 = logfile.readline(1)
            line2 = logfile.readline(2)
            line3 = logfile.readline(3)
            line4 = logfile.readline(4)
            line5 = logfile.readline(5)
            line6 = logfile.readline(6)
            line7 = logfile.readline(7)
            line8 = logfile.readline(8)
            line9 = logfile.readline(9)
            line10 = logfile.readline(10)
            encrypt1 = flr2str.replace("a", line4[15:])
            encrypt2 = encrypt1.replace("b", line7[:14])
            encrypt3 = encrypt2.replace("c", line1[23:])
            encrypt4 = encrypt3.replace("d", line8[2:])
            encrypt5 = encrypt4.replace("e", line10[13:])
            encrypt6 = encrypt5.replace("f", line6[:24])
            encrypt7 = encrypt6.replace("g", line8[:32])
            encrypt8 = encrypt7.replace("h", line3[24:])
            encrypt9 = encrypt8.replace("i", line2[:36])
            encrypt10 = encrypt9.replace("j", line9[:42])
            encrypt11 = encrypt10.replace("k", line5[17:])
            encrypt12 = encrypt11.replace("l", line2[34:])
            encrypt13 = encrypt12.replace("m", line8[38:])
            encrypt14 = encrypt13.replace("n", line2[:2])
            encrypt15 = encrypt14.replace("o", line3[:4])
            encrypt16 = encrypt15.replace("p", line5[5:])
            encrypt17 = encrypt16.replace("q", line6[:3])
            encrypt18 = encrypt17.replace("r", line8[24:])
            encrypt19 = encrypt18.replace("s", line2[2:])
            encrypt20 = encrypt19.replace("t", line5[:21])
            encrypt21 = encrypt20.replace("u", line10[:25])
            encrypt22 = encrypt21.replace("v", line4[16:])
            encrypt23 = encrypt22.replace("w", line6[:21])
            encrypt24 = encrypt23.replace("y", line1[14:])
            encrypt25 = encrypt24.replace("x", line3[32:])
            encrypt26 = encrypt25.replace("z", line7[:12])
            tw = open("test.txt", "w")
            tw.write(encrypt26)


        else:
            encryptionstarted.configure(text="you need to input your file", text_color="red")

    elif filelocationcheck == True:
        encryptionstarted.configure(text="Generate your key", text_color="red")
    else:
        encryptionstarted.configure(text="You need to generate key and input file", text_color="red")

def keygenerator():
    global keygenerated
    global key1str
    global key2str
    global key3str
    global key4str
    global key5str
    global key6str
    global key7str
    global key8str
    global key9str
    global key10str

    script_dir = os.path.dirname(os.path.abspath(__file__))
    if keygenerated == False:
        if plusoneonlog == True:
            new_file_path = os.path.join(script_dir, 'logfile1')
        else: 
            new_file_path = os.path.join(script_dir, 'logfile')
            keygenerated = not False
            key1 = random.getrandbits(256)
            key2 = random.getrandbits(256)
            key3 = random.getrandbits(368)
            key4 = random.getrandbits(373)
            key5 = random.getrandbits(254)
            key6 = random.getrandbits(253)
            key7 = random.getrandbits(353)
            key8 = random.getrandbits(482)
            key9 = random.getrandbits(552)
            key10 = random.getrandbits(325)
            key10str = str(key10)
            key9str = str(key9)
            key8str = str(key8)
            key7str = str(key7)
            key6str = str(key6)
            key1str = str(key1)
            key2str = str(key2)
            key3str = str(key3)
            key4str = str(key4)
            key5str = str(key5)
            with open(new_file_path, 'w') as file:
                file.write(key1str + "\n" + key2str + "\n" + key3str + "\n" + key4str + "\n" + key5str + "\n" + key6str + "\n" + key7str + "\n" + key8str + "\n" + key9str + "\n" + key10str)
            keygeneratedlbl.configure(text="Key has been generated", text_color="green")
            keygeneratedlbl2.configure(text="  Check log file", text_color="green")
    else:
        anyerror.configure(text="Already generated a key")




mainwindow = customtkinter.CTk()
mainwindow.geometry("400x400")
mainwindow.title("Dropz Encryption")


header = customtkinter.CTkLabel(master=mainwindow, text="Dropz Encryption")
header.place(relx=.5, rely=.2, anchor="center")

keygeneration = customtkinter.CTkButton(mainwindow, text="Generate keys", command=keygenerator)
keygeneration.place(relx=.5, rely=.3, anchor="center")

keygeneratedlbl = customtkinter.CTkLabel(mainwindow, text=" ", font=("roboto", 10))
keygeneratedlbl.place(relx=.03, rely=.2)
keygeneratedlbl2 = customtkinter.CTkLabel(mainwindow, text=" ")
keygeneratedlbl2.place(relx=.05, rely=.27)

filetoencrypt = customtkinter.CTkButton(mainwindow, text="File to encrypt", command=filename)
filetoencrypt.place(relx=.5, rely=.4, anchor="center")
filenamelbl = customtkinter.CTkLabel(mainwindow, text=" ")
filenamelbl.place(relx=.2, rely=.8, anchor="center")


encryptbtn = customtkinter.CTkButton(mainwindow, text="encrypt", command=encrypt)
encryptbtn.place(relx=.5, rely=.5, anchor="center")

anyerror = customtkinter.CTkLabel(mainwindow, text=" ", text_color="red")
anyerror.place(relx=.5, rely=.1, anchor="center")

encryptionstarted = customtkinter.CTkLabel(mainwindow, text=" ", text_color="green")
encryptionstarted.place(relx=.5, rely=.7, anchor="center")

filelbl = customtkinter.CTkLabel(mainwindow, text=" ", text_color="green")
filelbl.place(relx=.8, rely=.27, anchor="center")
if foundinlog == True:
    keygeneratedlbl.configure(text="Key found in log", text_color="green")
mainwindow.mainloop()
