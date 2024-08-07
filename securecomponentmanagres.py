import tkinter as tk
import subprocess
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import webbrowser
import sqlite3


connection = sqlite3.connect("passwords.db")
cursor = connection.cursor()

win = tk.Tk()
win.title("Security Component Manager")
win.geometry('1100x700')
win.configure(bg='black')
win.iconbitmap(r'C:\Users\batch\favicon.ico')

button_frame = tk.Frame(win, bg='white')



#  batch file paths
usb_disable = r'C:\Users\batch\usb_disable.bat'
usb_enable = r'C:\Users\batch\usb_enable.bat'
camera_disable = r'C:\Users\batch\camera_disable.bat'
camera_enable = r'C:\Users\batch\camera_enable.bat'
keyboard_disable = r'C:\Users\batch\keyboard_disable.bat'
keyboard_enable = r'C:\Users\batch\keyboard_enable.bat'
wifi_enable = r'C:\Users\batch\wifi_enable.bat' 
wifi_disable = r'C:\Users\batch\wifi_disable.bat'
touchpad_enable = r'C:\Users\batch\touchpad_enable.bat'
touch_disable = r'C:\Users\batch\touchpad_disable.bat'


global_usbenablepass = ""
#password get for camera
def get_password_camera():
    global global_usbenablepass 
    get_pass = tk.Toplevel(win)
    get_pass.iconbitmap(r'C:\Users\batch\favicon.ico')
    get_pass.title("Create Password")
    get_pass.geometry("300x200")
    get_label = tk.Label(get_pass, text="Create password here")
    get_label.pack()
    get_entry = tk.Entry(get_pass, show="")
    get_entry.pack()

    def okey():
        global global_usbenablepass 
        global_usbenablepass = get_entry.get()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='passwords';")
        table_exists = cursor.fetchone()

        if not table_exists:
            # If the table doesn't exist, create it
            cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT);")
        cursor.execute("INSERT INTO passwords (password) VALUES (?)", (global_usbenablepass,))
        connection.commit()
        mass_label = tk.Label(camera_frame, text="Password created successfully", bg="black", fg="yellow")
        mass_label.pack()
        print(global_usbenablepass)
        get_pass.destroy()

    ok_button1 = tk.Button(get_pass, text="OK", bg="black", fg="white", command=okey)
    ok_button1.pack()

# the functions call for camera
def disable_camera():
    subprocess.run(r'C:\Users\batch\camera_disable.bat',shell=True)
    label1 = tk.Label(camera_frame,text="camera disable successful",font=("Arial", 8, "bold"),bg="black",fg="red")
    label1.pack(side="left",padx=5)
    
  
def enable_camera():
    password_win = tk.Toplevel(win)
    password_win.iconbitmap(r'C:\Users\batch\favicon.ico')
    password_win.title("Enter Password")
    password_win.geometry("300x200")
    password_label = tk.Label(password_win, text="Enter the password here")
    password_label.pack()
    password_enter = tk.Entry(password_win, show="*")
    password_enter.pack()

    def ok():
        global global_usbenablepass  
        entered_password = password_enter.get().strip()
        cursor.execute("SELECT password FROM passwords WHERE id = 3")
        stored_password_result = cursor.fetchone()
        print(entered_password)
        print(stored_password_result)
        if stored_password_result is not None:
            stored_password = stored_password_result[0]
            print("Entered password:", entered_password)
            print("Stored password:", stored_password)
            if entered_password == stored_password:
                subprocess.run(r'C:\Users\batch\camera_enable.bat',shell=True)
                label2 = tk.Label(camera_frame, text="camera enabled successfully",font=("Arial", 8, "bold"), bg="black", fg="green")
                label2.pack(side="left", padx=5)
                password_win.destroy()
            else:
                error_label = tk.Label(camera_frame, text="Password is incorrect",font=("Arial", 8, "bold"), bg="black", fg="yellow")
                error_label.pack()
                password_enter.delete(0, tk.END)
        else:
        # Handle the case where no password is found in the database
            error_labell = tk.Label(usb_frame, text="No password found in the database", bg="black", fg="yellow")
            error_labell.pack()


    ok_button = tk.Button(password_win, text="ok", bg="black", fg="white", command=ok)
    ok_button.pack()


# Password input for usb
global_usbenablepass = ""
def get_password_usb():
    global global_usbenablepass 
    get_pass = tk.Toplevel(win)
    get_pass.iconbitmap(r'C:\Users\batch\favicon.ico')
    get_pass.title("Create Password")
    get_pass.geometry("300x200")
    get_label = tk.Label(get_pass, text="Create password here")
    get_label.pack()
    get_entry = tk.Entry(get_pass, show="")
    get_entry.pack()

    def okey():
        global global_usbenablepass 
        global_usbenablepass = get_entry.get()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='passwords';")
        table_exists = cursor.fetchone()

        if not table_exists:
            # If the table doesn't exist, create it
            cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT);")
        cursor.execute("INSERT INTO passwords (password) VALUES (?)", (global_usbenablepass,))
        connection.commit()
        mass_label = tk.Label(usb_frame, text="Password created successfully", bg="black", fg="yellow")
        mass_label.pack()
        print(global_usbenablepass)
        get_pass.destroy()

    ok_button1 = tk.Button(get_pass, text="ok", bg="black", fg="white", command=okey)
    ok_button1.pack()

# usb enable and disable
def disable_usb():
    subprocess.run(r'C:\Users\batch\usb_disable.bat',shell=True)
    label1 = tk.Label(usb_frame, text="usb disabled successfully",font=("Arial", 8, "bold"), bg="black", fg="red")
    label1.pack(side="left", padx=5)

def enable_usb():
    password_win = tk.Toplevel(win)
    password_win.iconbitmap(r'C:\Users\batch\favicon.ico')
    password_win.title("Enter Password")
    password_win.geometry("300x200")
    password_label = tk.Label(password_win, text="Enter the password here")
    password_label.pack()
    password_enter = tk.Entry(password_win, show="*")
    password_enter.pack()

    def ok():
        global global_usbenablepass  
        entered_password = password_enter.get().strip()
        cursor.execute("SELECT password FROM passwords WHERE id = 3")  # Assuming the password is stored in the first row
        stored_password_result = cursor.fetchone()
        print(entered_password)
        print(stored_password_result)
        if stored_password_result is not None:
            stored_password = stored_password_result[0]
            print("Entered password:", entered_password)
            print("Stored password:", stored_password)

            if entered_password == stored_password:
                subprocess.run(r'C:\Users\batch\usb_enable.bat',shell=True)
                label2 = tk.Label(usb_frame, text="usb enabled successfully",font=("Arial", 8, "bold"), bg="black", fg="green")
                label2.pack(side="left", padx=5)
                password_win.destroy()
            else:
                error_label = tk.Label(usb_frame, text="Password is incorrect",font=("Arial", 8, "bold"), bg="black", fg="yellow")
                error_label.pack()
                password_enter.delete(0, tk.END)
        else:
        # Handle the case where no password is found in the database
            error_labell = tk.Label(usb_frame, text="No password found in the database", bg="black", fg="yellow")
            error_labell.pack()

    ok_button = tk.Button(password_win, text="ok", bg="black", fg="white", command=ok)
    ok_button.pack()



#password get for keyboard
global_keyboardpass = ""
def get_password_keyboard():
    get_pass = tk.Toplevel(win)
    get_pass.iconbitmap(r'C:\Users\batch\favicon.ico')
    get_pass.title("create password")
    get_pass.geometry("300x200")
    get_label = tk.Label(get_pass,text="create password here")
    get_label.pack()
    get_entry = tk.Entry(get_pass,show="")
    get_entry.pack()
    def okey():
        global global_keyboardpass
        global_keyboardpass = get_entry.get()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='passwords';")
        table_exists = cursor.fetchone()

        if not table_exists:
            # If the table doesn't exist, create it
            cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT);")
        cursor.execute("INSERT INTO passwords (password) VALUES (?)", (global_keyboardpass,))
        connection.commit()
        mass_label = tk.Label(keyboard_frame, text="Password created successfully", bg="black", fg="yellow")
        mass_label.pack()
        print(global_keyboardpass)
        get_pass.destroy()

    ok_button1 = tk.Button(get_pass,text="ok",bg="black",fg="white",command=okey)
    ok_button1.pack()


# keyboard enable and disable 
def disable_keyboard():
    subprocess.run(r'C:\Users\batch\keyboard_disable.bat',shell=True)
    label1 = tk.Label(keyboard_frame,text="keyboard disable successful",font=("Arial", 8, "bold"),bg="black",fg="red")
    label1.pack(side="left",padx=5)

def enable_keyboard():
    password_win = tk.Toplevel(win)
    password_win.iconbitmap(r'C:\Users\batch\favicon.ico')
    password_win.title("enter password")
    password_win.geometry("300x200")
    password_label=tk.Label( password_win,text="enter the password here")
    password_label.pack()
    password_enter=tk.Entry(password_win,show="$")
    password_enter.pack()
    def ok():
        global global_keyboardpass
        entered_password = password_enter.get().strip()
        cursor.execute("SELECT password FROM passwords WHERE id = 3")  # Assuming the password is stored in the first row
        stored_password_result = cursor.fetchone()
        print(entered_password)
        print(stored_password_result)
        if stored_password_result is not None:
            stored_password = stored_password_result[0]
            print("Entered password:", entered_password)
            print("Stored password:", stored_password)
            if entered_password == stored_password:
                subprocess.run(r'C:\Users\batch\keyboard_enable.bat',shell=True)
                label2=tk.Label(keyboard_frame,text="keyboard enable successfull",font=("Arial", 8, "bold"),bg="black",fg="green")
                label2.pack(side="left",padx=5)
                password_win.destroy()
            else:
                error_label = tk.Label(keyboard_frame,text="password si incorrect",font=("Arial", 8, "bold"),bg="black",fg="yellow")
                error_label.pack()
                password_enter.delete(0,tk.END)
        else:
        # Handle the case where no password is found in the database
            error_labell = tk.Label(usb_frame, text="No password found in the database", bg="black", fg="yellow")
            error_labell.pack()

            
    ok_button = tk.Button(password_win,text="ok",bg="black",fg="white",command=ok)
    ok_button.pack()



# password get for wifi
global_wifienablepass = ""
def get_password_wifi():
    get_pass = tk.Toplevel(win)
    get_pass.iconbitmap(r'C:\Users\batch\favicon.ico')
    get_pass.title("create password")
    get_pass.geometry("300x200")
    get_label = tk.Label(get_pass,text="create password here")
    get_label.pack()
    get_entry = tk.Entry(get_pass,show="")
    get_entry.pack()
    def okey():
        global global_wifienablepass
        global_wifienablepass = get_entry.get()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='passwords';")
        table_exists = cursor.fetchone()

        if not table_exists:
            # If the table doesn't exist, create it
            cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT);")
        cursor.execute("INSERT INTO passwords (password) VALUES (?)", (global_wifienablepass,))
        connection.commit()
        mass_label = tk.Label(wifi_frame, text="Password created successfully", bg="black", fg="yellow")
        mass_label.pack()
        print(global_wifienablepass)
        get_pass.destroy()

    ok_button1 = tk.Button(get_pass,text="ok",bg="black",fg="white",command=okey)
    ok_button1.pack()
   
#wifi enable and disable 
def disable_wifi():
    subprocess.run(r'C:\Users\batch\wifi_disable.bat',shell=True)
    label1 = tk.Label(wifi_frame,text="wifi disable successful",font=("Arial", 8, "bold"),bg="black",fg="red")
    label1.pack(side="left",padx=5)

    
def enable_wifi():
    password_win = tk.Toplevel(win)
    password_win.iconbitmap(r'C:\Users\batch\favicon.ico')
    password_win.title("enter password")
    password_win.geometry("300x200")
    password_label=tk.Label( password_win,text="enter the password here")
    password_label.pack()
    password_enter=tk.Entry(password_win,show="$")
    password_enter.pack()
    def ok():
        global global_wifienablepass
        entered_password = password_enter.get().strip()
        cursor.execute("SELECT password FROM passwords WHERE id = 3")  # Assuming the password is stored in the first row
        stored_password_result = cursor.fetchone()
        print(entered_password)
        print(stored_password_result)
        if stored_password_result is not None:
            stored_password = stored_password_result[0]
            print("Entered password:", entered_password)
            print("Stored password:", stored_password)
            if entered_password ==  stored_password:
                subprocess.run(r'C:\Users\batch\wifi_enable.bat',shell=True)
                label2=tk.Label(wifi_frame,text="wifi enable successfull",font=("Arial", 8, "bold"),bg="black",fg="green")
                label2.pack(side="left",padx=5)
                password_win.destroy()
            else:
                error_label = tk.Label(wifi_frame,text="password si incorrect",font=("Arial", 8, "bold"),bg="black",fg="yellow")
                error_label.pack()
                password_enter.delete(0,tk.END)
        else:
        # Handle the case where no password is found in the database
            error_labell = tk.Label(usb_frame, text="No password found in the database", bg="black", fg="yellow")
            error_labell.pack()

            
    ok_button = tk.Button(password_win,text="ok",bg="black",fg="white",command=ok)
    ok_button.pack()



#password get for mousepad
global_touchpad = ""
def get_password_mousepad():
    get_pass = tk.Toplevel(win)
    get_pass.iconbitmap(r'C:\Users\batch\favicon.ico')
    get_pass.title("create password")
    get_pass.geometry("300x200")
    get_label = tk.Label(get_pass,text="create password here")
    get_label.pack()
    get_entry = tk.Entry(get_pass,show="")
    get_entry.pack()
    def okey():
        global global_touchpad
        global_touchpad = get_entry.get()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='passwords';")
        table_exists = cursor.fetchone()

        if not table_exists:
            # If the table doesn't exist, create it
            cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT);")
        cursor.execute("INSERT INTO passwords (password) VALUES (?)", (global_touchpad,))
        connection.commit()
        mass_label = tk.Label(mousepad_frame, text="Password created successfully", bg="black", fg="yellow")
        mass_label.pack()
        print(global_touchpad)
        get_pass.destroy()

    ok_button1 = tk.Button(get_pass,text="ok",bg="black",fg="white",command=okey)
    ok_button1.pack()

    

#touchpad enable and disable 
def disable_touchpad():
    subprocess.run(r'C:\Users\batch\touchpad_disable.bat',shell=True)
    label1 = tk.Label(mousepad_frame,text="touchpad disable successful",font=("Arial", 8, "bold"),bg="black",fg="red")
    label1.pack(side="left",padx=5)
    
def enable_touchpad():
    password_win = tk.Toplevel(win)
    password_win.iconbitmap(r'C:\Users\batch\favicon.ico')
    password_win.title("enter password")
    password_win.geometry("300x200")
    password_label=tk.Label( password_win,text="enter the password here")
    password_label.pack()
    password_enter=tk.Entry(password_win,show="$")
    password_enter.pack()
    def ok():
        global global_touchpad
        entred_password = password_enter.get().strip()
        cursor.execute("SELECT password FROM passwords WHERE id = 3")  # Assuming the password is stored in the first row
        stored_password_result = cursor.fetchone()
        print(entred_password)
        print(stored_password_result)
        if stored_password_result is not None:
            stored_password = stored_password_result[0]
            print("Entered password:",entred_password)
            print("Stored password:", stored_password)
            if entred_password == stored_password:
                print(global_touchpad)
                print(entred_password)
                subprocess.run(r'C:\Users\batch\touchpad_enable.bat',shell=True)
                label2=tk.Label(mousepad_frame,text="touchpad enable successfull",font=("Arial", 8, "bold"),bg="black",fg="green")
                label2.pack(side="left",padx=5)
                password_win.destroy()
            else:
                error_label = tk.Label(mousepad_frame,text="password si incorrect",font=("Arial", 8, "bold"),bg="black",fg="yellow")
                error_label.pack()
                password_enter.delete(0,tk.END)
        else:
        # Handle the case where no password is found in the database
            error_labell = tk.Label(usb_frame, text="No password found in the database", bg="black", fg="yellow")
            error_labell.pack()
            
    ok_button = tk.Button(password_win,text="ok",bg="black",fg="white",command=ok)
    ok_button.pack()


#password get for lan
global_lanpass = ""
def get_password_lan():
    get_pass = tk.Toplevel(win)
    get_pass.iconbitmap(r'C:\Users\batch\favicon.ico')
    get_pass.title("create password")
    get_pass.geometry("300x200")
    get_label = tk.Label(get_pass,text="create password here")
    get_label.pack()
    get_entry = tk.Entry(get_pass,show="")
    get_entry.pack()
    def okey():
        global global_lanpass
        global_lanpass = get_entry.get()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='passwords';")
        table_exists = cursor.fetchone()

        if not table_exists:
            # If the table doesn't exist, create it
            cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT);")
        cursor.execute("INSERT INTO passwords (password) VALUES (?)", (global_lanpass,))
        connection.commit()
        mass_label = tk.Label(lan_frame, text="Password created successfully", bg="black", fg="yellow")
        mass_label.pack()
        print(global_lanpass)
        get_pass.destroy()

    ok_button1 = tk.Button(get_pass,text="ok",bg="black",fg="white",command=okey)
    ok_button1.pack()

#enable and disable lan
def disable_lan():
    subprocess.run(r'C:\Users\batch\lan_disable.bat',shell=True)
    label1 = tk.Label(lan_frame,text="lan disable successful",font=("Arial", 8, "bold"),bg="black",fg="red")
    label1.pack(side="left",padx=5)
    
def enable_lan():
    password_win = tk.Toplevel(win)
    password_win.iconbitmap(r'C:\Users\batch\favicon.ico')
    
    password_win.title("enter password")
    password_win.geometry("300x200")
    password_label=tk.Label( password_win,text="enter the password here")
    password_label.pack()
    password_enter=tk.Entry(password_win,show="$")
    password_enter.pack()
    def ok():
        global global_lanpass
        entred_password = password_enter.get().strip()
        cursor.execute("SELECT password FROM passwords WHERE id = 3")  # Assuming the password is stored in the first row
        stored_password_result = cursor.fetchone()
        print(entred_password)
        print(stored_password_result)
        if stored_password_result is not None:
            stored_password = stored_password_result[0]
            print("Entered password:", entred_password)
            print("Stored password:", stored_password)
            if entred_password == stored_password:
                print(global_lanpass)
                print(entred_password)
                subprocess.run(r'C:\Users\batch\lan_enable.bat',shell=True)
                label2=tk.Label(lan_frame,text="lan enable successfull",font=("Arial", 8, "bold"),bg="black",fg="green")
                label2.pack(side="left",padx=5)
                password_win.destroy()
            else:
                error_label = tk.Label(lan_frame,text="password si incorrect",font=("Arial", 8, "bold"),bg="black",fg="yellow")
                error_label.pack()
                password_enter.delete(0,tk.END)
        else:
        # Handle the case where no password is found in the database
            error_labell = tk.Label(usb_frame, text="No password found in the database", bg="black", fg="yellow")
            error_labell.pack()
            
    ok_button = tk.Button(password_win,text="ok",bg="black",fg="white",command=ok)
    ok_button.pack()

def update_password():
    get_pass = tk.Toplevel(win)
    get_pass.iconbitmap(r'C:\Users\batch\favicon.ico')
    get_pass.title("Update Password")
    get_pass.geometry("300x200")
    get_label = tk.Label(get_pass, text="Enter old password")
    get_label.pack()
    get_entryold = tk.Entry(get_pass,)
    get_entryold.pack()
    get_label = tk.Label(get_pass, text="Enter new password")
    get_label.pack()
    get_entry = tk.Entry(get_pass, show="..")
    get_entry.pack()
    def okey():
        old_password = get_entryold.get()
        cursor.execute("SELECT * FROM passwords WHERE id = ? AND password = ?", (3, old_password))

        # Check if the old password is correct
        if cursor.fetchone():
            new_password = get_entry.get()
            cursor.execute("UPDATE passwords SET password = ? WHERE id = ?", (new_password, 3))
            connection.commit()
            print("Password updated successfully")
            mass_label = tk.Label(usb_frame, text="Password updated successfully", bg="black", fg="yellow")
            mass_label.pack()
            get_pass.destroy()
        else:
            messagebox.showerror("Error", "Old password is incorrect")


    ok_button1 = tk.Button(get_pass, text="OK", bg="black", fg="white", command=okey)
    ok_button1.pack()

#project info
def info():
    projectinfo = r'https://infoofdevolopers.netlify.app'
    webbrowser.open(projectinfo)

#website

def site():
    website = r'https://secure-component-managress.netlify.app/' 
    webbrowser.open(website)

    


label_main = tk.Label(win, text=" Security component manager", font=("Arial", 18, "bold"), bg="black", fg="white")
label_main.pack(pady=20)
                          
#gap frame
gap_frame = tk.Frame(win, bg='black', height=100)
gap_frame.pack(anchor='w')

#use
usb_frame = tk.Frame(win, bg='black')
usb_frame.pack(anchor='w')
usb_label = tk.Label(usb_frame, text=("\tUSB\t\t\t\t"+"                  "), font=("Arial", 12, "bold"), bg="black", fg="white")
usb_label.pack(side='left',anchor='w')
usb_disable_button = tk.Button(usb_frame, text=("Disable"), bg="red", fg="white",command=disable_usb)
usb_disable_button.pack(side='left', padx=10)
usb_enable_button = tk.Button(usb_frame, text="Enable", bg="green", fg="white",command=enable_usb)
usb_enable_button.pack(side='left', padx=10)
usb_password = tk.Button(usb_frame,text="set password",bg="blue",fg="white",command=get_password_usb)
usb_password.pack(side="left",padx=10)
update = tk.Button(usb_frame,text='updatepassword',bg="blue",fg="white",command=update_password)
update.pack(side='left')
                         


gap_frame = tk.Frame(win, bg='black', height=10)
gap_frame.pack(anchor='w')

#camera
camera_frame = tk.Frame(win, bg='black')
camera_frame.pack(anchor='w')
camera_label = tk.Label(camera_frame, text=("\tCamera\t\t\t\t"+"                  "), font=("Arial", 12, "bold"), bg="black", fg="white")
camera_label.pack(side='left',anchor='w')
camera_disable_button = tk.Button(camera_frame, text="Disable", bg="red", fg="white",command=disable_camera)
camera_enable_button = tk.Button(camera_frame, text="Enable", bg="green", fg="white" ,command=enable_camera)
camera_disable_button.pack(side='left', padx=10)
camera_enable_button.pack(side='left', padx=10)
camera_password = tk.Button(camera_frame,text="set password",bg="blue",fg="white",command=get_password_camera)
camera_password.pack(side="left",padx=10)
update = tk.Button(camera_frame,text='updatepassword',bg="blue",fg="white",command=update_password)
update.pack(side='left')

gap_frame = tk.Frame(win, bg='black', height=10)
gap_frame.pack(anchor='w')


# Wi-Fi
wifi_frame = tk.Frame(win, bg='black',width='90')
wifi_frame.pack(anchor='w')
wifi_label = tk.Label(wifi_frame, text=("\tWi-Fi\t\t\t\t"+"                  "), font=("Arial", 12, "bold"), bg="black", fg="white")
wifi_label.pack(side='left',anchor='w')
wifi_disable_button = tk.Button(wifi_frame, text="Disable", bg="red", fg="white",command=disable_wifi)
wifi_disable_button.pack(side='left', padx=10)
wifi_enable_button = tk.Button(wifi_frame, text="Enable", bg="green", fg="white",command=enable_wifi)
wifi_enable_button.pack(side='left', padx=10)
wifi_password = tk.Button(wifi_frame,text="set password",bg="blue",fg="white",command=get_password_wifi)
wifi_password.pack(side="left",padx=10)
update = tk.Button(wifi_frame,text='updatepassword',bg="blue",fg="white",command=update_password)
update.pack(side='left')


gap_frame = tk.Frame(win, bg='black', height=10)
gap_frame.pack(anchor='w')

# Mousepad
mousepad_frame = tk.Frame(win, bg='black')
mousepad_frame.pack(anchor='w')
mousepad_label = tk.Label(mousepad_frame, text=("\tMousepad\t\t\t\t"), font=("Arial", 12, "bold"), bg="black", fg="white")
mousepad_label.pack(side='left',anchor='w')
mousepad_disable_button = tk.Button(mousepad_frame, text="Disable", bg="red", fg="white",command=disable_touchpad)
mousepad_disable_button.pack(side='left', padx=10)
mousepad_enable_button = tk.Button(mousepad_frame, text="Enable", bg="green", fg="white",command=enable_touchpad)
mousepad_enable_button.pack(side='left', padx=10)
mousepad_password = tk.Button(mousepad_frame,text="set password",bg="blue",fg="white",command=get_password_mousepad)
mousepad_password.pack(side="left",padx=10)
update = tk.Button(mousepad_frame,text='updatepassword',bg="blue",fg="white",command=update_password)
update.pack(side='left')

gap_frame = tk.Frame(win, bg='black', height=10)
gap_frame.pack(anchor='w')

#Keyboard
keyboard_frame =  tk.Frame(win, bg='black')
keyboard_frame.pack(anchor='w')
keyboard_label = tk.Label(keyboard_frame, text=("\tKeyboard\t\t\t\t"), font=("Arial", 12, "bold"), bg="black", fg="white")
keyboard_label.pack(side='left',anchor='w')
keyboard_disable_button = tk.Button(keyboard_frame, text="Disable", bg="red", fg="white",command=disable_keyboard)
keyboard_disable_button.pack(side='left', padx=10)
keyboard_enable_button = tk.Button(keyboard_frame, text="Enable", bg="green", fg="white",command=enable_keyboard)
keyboard_enable_button.pack(side='left', padx=10)
keyboard_password = tk.Button(keyboard_frame,text="set password",bg="blue",fg="white",command=get_password_keyboard)
keyboard_password.pack(side="left",padx=10)
update = tk.Button(keyboard_frame,text='updatepassword',bg="blue",fg="white",command=update_password)
update.pack(side='left')

gap_frame = tk.Frame(win, bg='black', height=10)
gap_frame.pack(anchor='w')

#LAN
lan_frame = tk.Frame(win, bg='black')
lan_frame.pack(anchor='w')
lan_label = tk.Label(lan_frame, text=("\tLAN\t\t\t\t"+"                  "), font=("Arial", 12, "bold"), bg="black", fg="white")
lan_label.pack(side='left',anchor='w')
lan_disable_button = tk.Button(lan_frame, text="Disable", bg="red", fg="white",command=disable_lan)
lan_disable_button.pack(side='left', padx=10)
lan_enable_button = tk.Button(lan_frame, text="Enable", bg="green", fg="white",command=enable_lan)
lan_enable_button.pack(side='left', padx=10)
lan_password = tk.Button(lan_frame,text="set password",bg="blue",fg="white",command=get_password_lan)
lan_password.pack(side="left",padx=10)
update = tk.Button(lan_frame,text='updatepassword',bg="blue",fg="white",command=update_password)
update.pack(side='left')
#memu button
lan = tk.Label(win, text=("\t"+"  "), font=("Arial", 12, "bold"), bg="black", fg="white")
lan.pack(side='left',anchor='w')

menu_frame = tk.Frame(win,bg='black')
menu_frame.pack(anchor='w')
#menu_button = tk.Button(win, text=("menu"),bg="red",fg="white")
#menu_button.pack(side="left",padx=50,pady=100,ipadx=20,ipady=4,anchor="w")

project_info = tk.Button(win, text="project info", bg="red", fg="white", command=info)
project_info.pack(side="left", padx=5, ipadx=20, ipady=4)

more  = tk.Button(win,text="More",bg="red",fg="white", command=site)
more.pack(side="left",padx=50,ipadx=20,ipady=4)




#image frame
image_frame = tk.Frame(win)
image_frame.pack()
image_path = 'C:\\Users\\batch\\backgrade1.png'
image = Image.open(image_path)
image = ImageTk.PhotoImage(image)
image_label = tk.Label(win, image=image,bg="black")
image_label.pack(side="top",anchor="se",padx=50,pady=50)
#image.place(relx=0.4,rely=1)


win.mainloop()
connection.close()
