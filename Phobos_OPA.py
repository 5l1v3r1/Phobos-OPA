import os #run some commands
from subprocess import * #capture the output of a command and print it into the GUI
import webbrowser #just for help to redirect to github project page
from sys import platform #avoid error(s) on unsupported commands
import subprocess
import requests, zipfile, io

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
root.geometry('750x450')
root.iconbitmap('Phobos_Logo.ico')
root.resizable(0,0)
i = tk.IntVar()
str = StringVar()
current_version = 1.13
#end of the gui propertie
#print the welcoming message in the terminal/cmd

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
    url = "https://github.com/kleiton0x00/phobos-opa"
    webbrowser.open(url,new=1)

def encoder():
    root1 = tk.Tk()
    root1.title("Phobo OPA - Encoder")
    root1.geometry('800x600')
    root1.iconbitmap('Phobos_Logo.ico')
    root1.resizable(0,0)
    vbose = tk.IntVar()
    verbosing = ""
 
    def encode_entry():
        if vbose.get() == 1:
            verbosing = " -v"
        elif vbose.get() == 0:
            verbosing = ""

        if platform == "linux" or platform == "linux2":
            os.system("chmod +x test.py")
            encode_command = "./test.py -m " + decoder_entry.get() + verbosing
            if decoder_entry.get() == "":
                tkinter.messagebox.showwarning("Phobos OPA - Error Warning Message", "Please enter a value of Decoder!")
            else:
                os.system(encode_command)
                final_encode_command = subprocess.run(encode_command, capture_output=True)
                output_box.insert('1.0',final_encode_command)
        elif platform == "win32":
            encode_command = "py test.py -m " + decoder_entry.get() + verbosing
            if decoder_entry.get() == "":
                tkinter.messagebox.showwarning("Phobos OPA - Error Warning Message", "Please enter a value of Decoder!")
            else:
                os.system(encode_command)
                final_encode_command = subprocess.run(encode_command, capture_output=True)
                output_box.insert('1.0',final_encode_command)

    root1_frame = LabelFrame(root1, text="Tutorial")
    root1_frame.place(x=0, y=0)

    root1_frame2 = LabelFrame(root1, text="Message:")
    root1_frame2.place(x=0, y=40)

    root1_frame3 = LabelFrame(root1, text="Output:")
    root1_frame3.place(x=0, y=85)

    verbose_checkbox = tk.Checkbutton(root1_frame2, text="Verbose", variable=vbose)
    verbose_checkbox.grid(row=0, column=1)
   
    tutorial_label = tk.Label(root1_frame, text="This tab is used to find the hash using a message. Using this technique, you don't need any remote server (or a website to deal with).")
    tutorial_label.grid(row=0, column=0)

    decoder_entry= tk.Entry(root1_frame2, width=74)
    decoder_entry.grid(row=0, column=0)

    encode_button = tk.Button(root1_frame2, text = 'Encode', command=encode_entry)
    encode_button.grid(row=0, column=2)

    output_box = Text(root1_frame3, width=80, height=25)
    output_box.grid(row=0, column=0)

#---------------------------------------------------------------------------------------------------------

def oracle_customise():
    root3 = tk.Tk()
    root3.title("Phobo OPA - Developer Mode")
    root3.geometry('800x600')
    root3.iconbitmap('Phobos_Logo.ico')
    root3.resizable(0,0)

    #all functions for this window

    def apply_code():
        developer_code = oracle_box.get()
        print(developer_code)
        os.system(developer_code)

    #end of functions for this window

    root3_frame = LabelFrame(root3, text="Developer Mode")
    root3_frame.place(x=0, y=0)

    root3_frame1 = LabelFrame(root3, text="Ready?")
    root3_frame1.place(x=1, y=550)

    text_clarification = tk.Label(root3_frame, text="This section is adapted for the ones who wants to modify the script, to adapt the output, depending the situation you are facing with.")
    text_clarification.grid(row=0, column=0)

    oracle_box = Text(root3_frame, width=99, height=31)
    oracle_box.grid(row=1, column=0)

    attack_button = tk.Button(root3_frame1, text="Apply Code", command=apply_code)
    attack_button.grid(row=0, column=0)

#---------------------------------------------------------------------------------------------------------

def delete_entries():
    urltarget_entry.delete(0,END)
    host_entry.delete(0, END)
    cipher_entry.delete(0, END)
    length_block_cipher_entry.delete(0, END)
    cookie_entry.delete(0, END)
    error_entry.delete(0, END)
    script_output.delete('1.0', END)
    command_output.delete(0, END)

def check_update():
    version_file = open('version.txt', mode='r')
    old_version = float(version_file.read())
    version_file.close()

    version_request = requests.get("https://raw.githubusercontent.com/kleiton0x00/Phobos-OPA/master/version.txt")
    new_version = float(version_request.content)

    if old_version >= new_version:
        tkinter.messagebox.showinfo("Check for update", "No need to update, you are using the latest version.")
    if old_version < new_version:
        update = tkinter.messagebox.askquestion("Check for update", "There is a newer version, do you want to update?")
        if update == 'yes':
            if platform == "linux" or platform == "linux2":
                tkinter.messagebox.showinfo("Update", "The software will begin to update, please be patient.")
                current_path = os.getcwd()
                os.system("git clone https://github.com/kleiton0x00/Phobos-OPA.git")
                tkinter.messagebox.showinfo("Successful update", "Software successfuly updated, please restart the application.")
            if platform == "win32":
                current_directory = os.getcwd()  
                request = requests.get("https://github.com/kleiton0x00/Phobos-OPA/archive/master.zip")
                zip_file = zipfile.ZipFile(io.BytesIO(request.content))
                zip_file.extractall(current_directory)
                tkinter.messagebox.showinfo("Successful update", "File successfuly extracted in: " + current_directory)
                tkinter.messagebox.showinfo("Successful update", "Software successfuly updated, please restart the application.")

def begin():
    command_output.delete(0, END)
    script_output.delete('1.0', END)
    #setting up some conditions in case some entries are blank
    #first condiditon for verbose
    if verbose_check.get() == 1:
        verbose = " -v "
    if verbose_check.get() == 0:
        verbose = ""
#condition for error since its not required 
#input filters so user can input the right values for each entry
    if host_entry.get() == "":
        tkinter.messagebox.showwarning("Phobos OPA - Error Warning", "Please insert a valid value of Host!")

    if "http://" not in host_entry.get() and "https://" not in host_entry.get() and "." not in host_entry.get():
        tkinter.messagebox.showwarning("Phobos OPA - Error Warning", "The Host must start with [http://] or [https://]!")

    if urltarget_entry.get() == "":
        tkinter.messagebox.showwarning("Phobos OPA - Error Warning", "Please insert a valid value of Directory!")

    if "/" not in urltarget_entry.get() and "." not in urltarget_entry.get() and "?" not in urltarget_entry.get() and "=" not in urltarget_entry.get():
        tkinter.messagebox.showwarning("Phobos OPA - Error Warning", "Please insert a valid value of Directory including [/]")

    if cipher_entry.get() == "":
        tkinter.messagebox.showwarning("Phobos OPA - Error Warning", "Please insert a valid value of Cipher!")

    if length_block_cipher_entry.get() == "": 
        tkinter.messagebox.showwarning("Phobos OPA - Error Warning", "Please insert a valid value of Cookie Length and make sure it is an integer!")

    if error_entry.get() == "":
        error = ""
    else:
        error = " --error " + error_entry.get()
#condition for radiobutton to check the selected http methods
    if i.get() == "GET":
        method = " --method GET"
    if i.get() == "HEAD":
        method = " --method HEAD"
    if i.get() == "PORT":
        method = " --post POST"
    if i.get() == "PUT":
        method = " --method PUT"
    if i.get() == "DELETE":
        method = " --method DELETE"
    if i.get() == "CONNECT":
        method = " --method CONNECT"
    if i.get() == "OPTIONS":
        method = " --method OPTIONS"
    if i.get() == "TRACE":
        method = " --method TRACE"

#condiditon for cookie since its not required
    if cookie_entry.get() == "":
        cookie = ""
    else:
        cookie = " --cookie " + cookie_entry.get()

#define the system to execute the proper command
    if platform == "linux" or platform == "linux2":
        os.system("chmod +x exploit.py")
        command = "./exploit.py -c " + cipher_entry.get() + " -l " + length_block_cipher_entry.get() + " --host " + host_entry.get() + " -u " + urltarget_entry.get() + cookie + error + verbose + method
        os.system(command)
        final_command = subprocess.run(command, capture_output=True)
        command_output.insert(0, command)
        script_output.insert('1.0',final_command)

    elif platform == "win32":
        command = "py exploit.py -c " + cipher_entry.get() + " -l " + length_block_cipher_entry.get() + " --host " + host_entry.get() + " -u " + urltarget_entry.get() + cookie + error + verbose + method
        os.system(command)
        final_command = subprocess.run(command, capture_output=True)
        command_output.insert(0, command)
        script_output.insert('1.0',final_command)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Encoder", command=encoder)
filemenu.add_command(label="Developer Mode", command=oracle_customise, state=DISABLED)
filemenu.add_command(label="Clear all", command=delete_entries)
filemenu.add_separator()
filemenu.add_command(label="Check for update", command=check_update)
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="Main", menu=filemenu)

#define all frames (super important)
frame1 = LabelFrame(root, text="Required Entries")
frame1.place(x=180, y=0)

frame2 = LabelFrame(root, text="Optional Entries")
frame2.place(x=180, y=135)

frame3 = LabelFrame(root, text="HTTP Method")
frame3.place(x=500, y=130)

frame4 = LabelFrame(root, text="Command Output")
frame4.place(x=180, y=185)

frame5 = LabelFrame(root, text="")
frame5.place(x=0, y=0)

frame6 = LabelFrame(root, text="Script Result")
frame6.place(x=180, y=240)

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
i = StringVar()
i.set("GET")
method_option = OptionMenu(frame3, i, "GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE")
method_option.grid(row=0, column=0)

#optinal commands (verbose checkmark)
verbose_check = IntVar()
verbose = tk.Checkbutton(frame4, text="Verbose", variable=verbose_check)
verbose.grid(row=0, column=1)

#output textbox
script_output = Text(frame6, width=69, height=10)
script_output.grid(row=1, column=0)

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

credential_label = tk.Label(frame5, text="\n \n \n \n \n \nKleiton Kurti (C) 2019")
credential_label.grid(row=2, column=0)

#end of script to configure all the script
root.config(menu=menubar)
root.mainloop()
