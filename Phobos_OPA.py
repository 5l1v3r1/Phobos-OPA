import os
import webbrowser #just for help to redirect to github project page
from sys import platform #avoid error(s) on unsupported commands

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from os import path
from tkinter import ttk
import tkinter.messagebox 

import argparse

#setting up the whole gui properties
root = tk.Tk()
root.title("Phobos - OPA v.1.1")
root.geometry('760x350')
root.iconbitmap('Phobos_Logo.ico')
root.resizable(0,0)
i = tk.IntVar()
str = StringVar()
#end of the gui properties

#print the welcoming message in the terminal/cmd
banner = """██████╗ ██╗  ██╗ ██████╗ ██████╗  ██████╗ ███████╗               ██████╗ ██████╗  █████╗ 
██╔══██╗██║  ██║██╔═══██╗██╔══██╗██╔═══██╗██╔════╝              ██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║██║   ██║██████╔╝██║   ██║███████╗    █████╗    ██║   ██║██████╔╝███████║
██╔═══╝ ██╔══██║██║   ██║██╔══██╗██║   ██║╚════██║    ╚════╝    ██║   ██║██╔═══╝ ██╔══██║
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝███████║              ╚██████╔╝██║     ██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝               ╚═════╝ ╚═╝     ╚═╝  ╚═╝
                                                                                          """
print(banner)
print("Welcome to PHOBO - OPA, a GUI Software specifically made for Oracle Padding Attacks. Because the Software is still on development, all the output of the processes will be displayed here, so please don't close this window, as it may crash the program.")

#license
document_license = """Copyright (c) 2019 The Browser Pirates

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or cypyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in conection with the software or the use or other dealings in the software."""

#functions
def quit():
    global root
    root.quit()

def documentation():
    tkinter.messagebox.showinfo("Phobos OPA - Documentation & License", document_license)

def help():
    url = "https://github.com/TheBrowserPirates/Phobos-OPA/wiki"
    webbrowser.open(url,new=1)

def delete_entries():
    urltarget_entry.delete(0,END)
    host_entry.delete(0, END)
    cipher_entry.delete(0, END)
    length_block_cipher_entry.delete(0, END)
    cookie_entry.delete(0, END)
    command_output.delete(0, END)
    error_entry.delete(0, END)

def begin():
    command_output.delete(0, END)
    #setting up some conditions in case some entries are blank
    #first condiditon for verbose
    if verbose_check.get() == 1:
        verbose = " -v "
    if verbose_check.get() == 0:
        verbose = ""
#condition for error since its not required 
    if error_entry.get() == "":
        error = ""
    else:
        error = " --error " + error_entry.get()
#condition for radiobutton to check the selected http methods
    if i.get() == 1:
        method = "GET"
    if i.get() == 2:
        method = "HEAD"
    if i.get() == 3:
        method = "POST"
    if i.get() == 4:
        method = "PUT"
    if i.get() == 5:
        method = "DELETE"
    if i.get() == 6:
        method = "CONNECT"
    if i.get() == 7:
        method = "OPTIONS"
    if i.get() == 8:
        method = "TRACE"
    if i.get() == "":
        method = "GET"

#condiditon for cookie since its not required
    if cookie_entry.get() == "":
        cookie = ""
    else:
        cookie = " --cookie " + cookie_entry.get()

#define the system to execute the proper command
    if platform == "linux" or platform == "linux2":
        os.system("chmod +x exploit.py")
        command = "./exploit.py -c " + cipher_entry.get() + " -l " + length_block_cipher_entry.get() + " --host " + host_entry.get() + " -u " + urltarget_entry.get() + cookie + error + verbose + "--method " + method
    elif platform == "win32":
        command = "py exploit.py -c " + cipher_entry.get() + " -l " + length_block_cipher_entry.get() + " --host " + host_entry.get() + " -u " + urltarget_entry.get() + cookie + error + verbose + "--method " + method
    try:
        command_output.insert(0,command)
    except:
        command_output.insert(0, "ERROR")
    os.system(command)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="Main", menu=filemenu)

#define all frames (super important)
frame1 = LabelFrame(root, text="Required Entries")
frame1.place(x=180, y=0)

frame2 = LabelFrame(root, text="Optional Entires")
frame2.place(x=180, y=135)

frame3 = LabelFrame(root, text="HTTP Method")
frame3.place(x=180, y=185)

frame4 = LabelFrame(root, text="Output")
frame4.place(x=180, y=260)

frame5 = LabelFrame(root, text="")
frame5.place(x=0, y=0)

#help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Documentation", command=help)
#helpmenu.add_command(label="FAQ", command=faq)
helpmenu.add_command(label="License", command=documentation)
menubar.add_cascade(label="Help", menu=helpmenu)

#host input
host_entry= tk.Entry(frame1, width=40)
host_entry.grid(row=0, column=1)
host_label = tk.Label(frame1, text="* Host (http://example.com)")
host_label.grid(row=0, column=0)

#urltarget input
urltarget_entry= tk.Entry(frame1, width=40)
urltarget_entry.grid(row=1, column=1)
url_label = tk.Label(frame1, text="* Directory (/index.aspx?c=) ")
url_label.grid(row=1, column=0)

#cipher
cipher_label = tk.Label(frame1, text="* Chiper:")
cipher_label.grid(row=2, column=0)
cipher_entry = tk.Entry(frame1, width=40)
cipher_entry.grid(row=2, column=1)

#cipher length
cipher_length_label = tk.Label(frame1, text="* Length of Chiper:")
cipher_length_label.grid(row=3, column=0)
length_block_cipher_entry = tk.Entry(frame1, width=40,)
length_block_cipher_entry.grid(row=3, column=1)

#error
error_label = tk.Label(frame1, text="* Error:")
error_label.grid(row=4, column=0)
error_entry= tk.Entry(frame1, width=40)
error_entry.grid(row=4, column=1)

#cookie
cookie_label = tk.Label(frame2, text="Cookie:")
cookie_label.grid(row=0, column=0)
cookie_entry= tk.Entry(frame2, width=40)
cookie_entry.grid(row=0, column=1)

#creating all the radiobuttons for HTTP Methods
get = tk.Radiobutton(frame3, text="GET", value=1, variable=i)
get.grid(row=0, column=0)

head = tk.Radiobutton(frame3, text="HEAD", value=2, variable=i)
head.grid(row=0, column=1)

post = tk.Radiobutton(frame3, text="POST", value=3, variable=i)
post.grid(row=0, column=2)
#post.config(state='disabled')

put = tk.Radiobutton(frame3, text="PUT", value=4, variable=i)
put.grid(row=0, column=3)

delete = tk.Radiobutton(frame3, text="DELETE", value=5, variable=i)
delete.grid(row=1, column=0)

connect = tk.Radiobutton(frame3, text="CONNECT", value=6, variable=i)
connect.grid(row=1, column=1)

options = tk.Radiobutton(frame3, text="OPTIONS", value=7, variable=i)
options.grid(row=1, column=2)

trace = tk.Radiobutton(frame3, text="TRACE", value=8, variable=i)
trace.grid(row=1, column=3)

#optinal commands (verbose checkmark)
verbose_check = IntVar()
verbose = tk.Checkbutton(frame4, text=" Verbose", variable=verbose_check)
verbose.grid(row=0, column=1)

#output display
command = StringVar() 
command_output = Entry(frame4, textvariable=command, width=60) 
command_output.grid(row=0, column=0)

#all buttons
attack_button = tk.Button(frame4, text="Start attack", command=begin)
attack_button.grid(row=0, column=2)

delete_button = tk.Button(frame4, text = 'Clear all', command=delete_entries)
delete_button.grid(row=0, column=3)
  
phobos_wallpaper = PhotoImage(file="Phobos_Wallpaper.png")
wallpaper_label = Label(frame5, image=phobos_wallpaper)
wallpaper_label.grid(row=0, column=0)

#end of script to configure all the script
root.config(menu=menubar)
root.mainloop()