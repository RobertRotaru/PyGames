import tkinter as tk
import os.path
from tkinter import messagebox
from os import path

objects = []
window = tk.Tk()
window.withdraw()
window.title("Password Keeper")

# ****** WELCOME WINDOW ******

class welcomeWindow(object) :
    loop = False

    def __init__(self, master) :
        top = self.top = tk.Toplevel(master)
        top.title("Pass Keeper")
        top.geometry('600x170')
        top.resizable(width = False, height = False)

        f = open("Pass Keeper/welcomeText.txt", 'r')
        data = f.read()
        f.close()

        self.l1 = tk.Label(top, text = "Welcome to Pass Keeper!", font = ("Times", '20', "bold"), justify = 'center')
        self.l1.grid(row = 0, column = 0)
        self.l2 = tk.Label(top, text = data, font = ("Times", '14'), justify = 'center')
        self.l2.grid(row = 3, column = 0)
        self.b = tk.Button(top, text = "Close", command = self.close)
        self.b.config(height = 1, width = 10)
        self.b.place(relx = 0.9, rely = 0.9, anchor = "se")

    def close(self) :
        self.loop = True
        self.top.destroy()
        popupWindow(window)


# ****** CODE WINDOW ******

class popupWindow(object) :
    loop = False
    attempts = 0

    def __init__(self, master) :
        top = self.top = tk.Toplevel(master)
        top.title("Input Password")
        top.geometry('250x100')
        top.resizable(width = False, height = False)

        self.l = tk.Label(top, text = 'Add Your Code', font = ("Times", "14"), justify = 'center')
        self.l.pack()
        self.e = tk.Entry(top, show = '*', width = 20)
        self.e.pack(pady = 7)
        self.b = tk.Button(top, text = 'Enter', font = ("Times", "14"), command = self.cleanup)
        self.b.pack()
    
    def cleanup(self) :
        self.value = self.e.get()
        access = readfileCode()

        if self.value == access :
            self.loop = True
            self.top.destroy()
            window.deiconify() 
        else :
            self.attempts += 1
            if self.attempts == 5 :
                window.quit()
            self.e.delete(0, 'end')
            messagebox.showerror('Incorrect code', 'Incorrect code, attempts remaining %d' %(5 - self.attempts))

# ******* NEW CODE WINDOW *******

class newCodeWindow() :
    loop = False

    def __init__(self) :
        top = self.top = tk.Toplevel(window)
        top.title('Change the code')
        top.geometry('150x150')
        top.resizable(width = False, height = False)

        self.codeLabel = tk.Label(top, text = 'Enter a Digit Code', font = ("Times", "14"), justify = 'center')
        self.codeLabel.pack()
        self.codeEntry = tk.Entry(top, width = 10)
        self.codeEntry.pack(pady = 7)
        self.codeButton = tk.Button(top, text = "Submit", command = self.modify)
        self.codeButton.pack()
    
    def modify(self) :
        data = self.codeEntry.get()
        clearfileCode()
        writeInFileCode(data)
        self.loop = True
        self.top.destroy()


# ***** MAIN WINDOW *****

class entity_add :
    def __init__(self, master, s, u, p) :
        self.site = s
        self.password = p
        self.user = u
        self.window = master
    
    def write(self) : 
        f = open('pass.txt', "a")
        s = self.site
        u = self.user
        p = self.password

        encryptedS = ""
        encryptedU = ""
        encryptedP = ""
        for letter in s:
            if letter == ' ':
                encryptedS += ' '
            else:
                encryptedS += chr(ord(letter) + 5)

        for letter in u:
            if letter == ' ':
                encryptedU += ' '
            else:
                encryptedU += chr(ord(letter) + 5)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)
        f.write(encryptedS + ':' + encryptedU + ':' + encryptedP + '\n')
        f.close()

class entity_display :
    def __init__(self, master, s, u, p, i) :
        self.site = s
        self.user = u
        self.password = p
        self.i = i
        self.window = master

        dencryptedS = ""
        dencryptedU = ""
        dencryptedP = ""
        for letter in self.site:
            if letter == ' ':
                dencryptedS += ' '
            else:
                dencryptedS += chr(ord(letter) - 5)

        for letter in self.user:
            if letter == ' ':
                dencryptedU += ' '
            else:
                dencryptedU += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                dencryptedP += ' '
            elif letter != '\n' :
                dencryptedP += chr(ord(letter) - 5)

        self.label_site = tk.Label(self.window, text = dencryptedS, font = ("Times", "14"))
        self.label_user = tk.Label(self.window, text = dencryptedU, font = ("Times", "14"))
        self.label_pass = tk.Label(self.window, text = dencryptedP, font = ("Times", "14"))
        self.delete_button = tk.Button(self.window, text = 'X', fg = "red", command = self.delete)

    def display(self) :
        self.label_site.grid(row = 6 + self.i, sticky = 'W')
        self.label_user.grid(row = 6 + self.i, column = 1)
        self.label_pass.grid(row = 6 + self.i, column = 2, sticky = 'E')
        self.delete_button.grid(row = 6 + self.i, column = 3, sticky = 'E')

    def delete(self) :
        answer = tk.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?')

        if answer == 'yes' :
            for i in objects:
                i.destroy()
                
            f = open('pass.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('pass.txt', "w")
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self) :
        self.label_site.destroy()
        self.label_user.destroy()
        self.label_pass.destroy()
        self.delete_button.destroy()

# ***** FUNCTIONS *****

def onsumbit() :
    s = site.get()
    p = password.get()
    u = user.get()
    e = entity_add(window, s, u, p)
    e.write()
    site.delete(0, 'end')
    user.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Added entity', 'Successfully Added, \n' + 'Site: ' + s +'\nUsername:' + u + "\nPassword: " + p)
    readfile()

def clearfileCode() :
    f = open("code.txt","w")
    f.close()

def readfileCode() :
    f = open("code.txt","r+")
    data = f.read()
    return data

def writeInFileCode(string) :
    f = open("code.txt","a")
    f.write(string)
    f.close()

def newWindow() :
    newCodeWindow()

def readfile():
    f = open('pass.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(':')
        e = entity_display(window, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()

if path.exists("code.txt") == False :
    f = open("code.txt","x")
    writeInFileCode("1234")
    f.close()

welcomeWindow(window)

# **** GRAPHICS ****

entity_label = tk.Label(window, text = 'Add Entity', font=('Times', 14))
site_label = tk.Label(window, text = 'Site: ', font=('Times', 14))
user_label = tk.Label(window, text = 'Username: ', font=('Times', 14))
pass_label = tk.Label(window, text = 'Password: ', font=('Times', 14))
site = tk.Entry(window, font=('Times', 14))
user = tk.Entry(window, font=('Times', 14))
password = tk.Entry(window, show = "*", font=('Times', 14))
submit = tk.Button(window, text = "Add Pass", command = onsumbit, font=('Times', 14))

entity_label.grid(columnspan = 3, row = 0)
site_label.grid(row = 1, sticky = 'E')
user_label.grid(row = 2, sticky = 'E')
pass_label.grid(row = 3, sticky = 'E')

site.grid(columnspan = 3, row = 1, column = 1, padx = 2, pady = 2, sticky = 'W')
user.grid(columnspan = 3, row = 2, column = 1, padx = 2, pady = 2, sticky = 'W')
password.grid(columnspan = 3, row = 3, column = 1, padx = 2, pady = 2, sticky = 'W')

submit.grid(columnspan = 3, pady = 4)

site2_label = tk.Label(window, text = "Site: ", font=('Times', 14))
user2_label = tk.Label(window, text = "Username: ", font=('Times', 14))
pass2_label = tk.Label(window, text = "Password: ", font=('Times', 14))

site2_label.grid(row = 5)
user2_label.grid(row = 5, column = 1)
pass2_label.grid(row = 5, column = 2)

menuBar = tk.Menu(window)
submenu = tk.Menu(menuBar)
submenu.add_command(label = "Change code", command = newWindow)
submenu.add_separator()

menuBar.add_cascade(label = "Options", menu = submenu)
window.configure(menu = menuBar)

readfile()
window.mainloop()