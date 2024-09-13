
from cryptography.fernet import Fernet
import customtkinter
from customtkinter import filedialog

configfound = False
string = "Fillertxt"

def configlook():
    global key
    global configfound
    try: 
        with open("key.key", "rb") as f:
            keyy = f.read()
            key = Fernet(keyy)
            configfound = not False
            configlbl.configure(text="Config found", text_color="green")
    except:
        configlbl.configure(text="Config Generated", text_color="Green")
        configfound = not True
        keyy = Fernet.generate_key()
        key = Fernet(keyy)
        with open("key.key", "wb") as f:
            f.write(key)


def fileenc():
    filepath = filedialog.askopenfilename()
    if filepath.endswith(".txt", ".py", "html", "css", "js", "json"):
        with open(filepath, "r") as f:
            filecontents = f.read()
            print(filecontents)
            fileencfinished = key.encrypt(filecontents.encode())
            with open("file_encrypted.txt", "wb") as f:
                f.write(fileencfinished)
                writtenlbl.configure(text="Written to file_encrypted.txt", text_color="green")
    else:
        writtenlbl.configure(text="File type not supported", text_color="red")

def encyrpt():
    if string == "Fillertxt":
        writtenlbl.configure(text="No text entered", text_color="red")
    else:
        writtenlbl.configure(text="Written to Encrypted.txt", text_color="green")
        with open("Encrypted.txt", "wb") as f:
            encyrpttxt = key.encrypt(string.encode())
            f.write(encyrpttxt)

def decrypt():
    filename = filedialog.askopenfilename()
    if filename.endswith(".txt"):
        with open(filename, "rb") as f:
            filecontents = f.read()
            decryptfinished = key.decrypt(filecontents)
            with open("decrypted.txt", "wb") as f:
                f.write(decryptfinished)
                writtenlbl.configure(text="Written to decrypted.txt", text_color="green")
def ent_changed(*args):
    global string
    string = encyrptent.get()
    currenttext = f" current text: {string}"
    print(currenttext)

try:
    with open("key.key", "rb") as f:
        key = f.read()
except:
    pass

main = customtkinter.CTk()
main.geometry("500x500")
main.title("Encryptor and Decryptor")

header = customtkinter.CTkLabel(main, text="80dropz Encryptor", font=("Arial", 20))
header.place(relx=.5, rely=.2, anchor="center")

entrychanged = customtkinter.StringVar()
encyrptent = customtkinter.CTkEntry(main, placeholder_text=" Encrypt", textvariable=entrychanged)
encyrptent.place(relx=.5, rely=.4, anchor="center")
entrychanged.trace_add("write", ent_changed)

fileencbtn = customtkinter.CTkButton(main, text="Select File", command=fileenc, fg_color="dark green")
fileencbtn.place(relx=.3, rely=.6, anchor="center")

encrpybtn = customtkinter.CTkButton(main, text="Encrypt", command=encyrpt, fg_color="Green")
encrpybtn.place(relx=.3, rely=.5, anchor="center")

decryptbtn = customtkinter.CTkButton(main, text="Decrypt", command=decrypt, fg_color="Red")
decryptbtn.place(relx=.7, rely=.5, anchor="center")

configlbl = customtkinter.CTkLabel(main, text=" ", text_color="green", font=("Arial", 14))
configlbl.place(relx=.2, rely=.05, anchor="center")

writtenlbl = customtkinter.CTkLabel(main, text=" ", text_color="green", font=("Arial", 14))
writtenlbl.place(relx=.5, rely=.93, anchor="center")
if __name__ == "__main__":
    configlook()

main.mainloop()


def configlook():
    global key
    global configfound
    try: 
        with open("key.key", "rb") as f:
            keyy = f.read()
            key = Fernet(keyy)
            configfound = not False
            configlbl.configure(text="Config found", text_color="green")
    except:
        configlbl.configure(text="Config Generated", text_color="Green")
        configfound = not True
        key = Fernet.generate_key()
        with open("key.key", "wb") as f:
            f.write(key)
