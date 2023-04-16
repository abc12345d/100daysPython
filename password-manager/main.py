# import * only import classes and constants, but messagebox is a module
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

DEFAULT_EMAIL = "abc@gmail.com"
UPPER_CASES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWER_CASES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS = list(range(10))
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showwarning(title='Oops', message= "Please don't leave 'Website' field empty!")
    else:
        try:
            with open('data.json','r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title='Error', message= "No Data File Found.")
        else:
            if website in data.keys():
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message= f'Email: {email}\n'+ f'Password: {password}')
            else:
                messagebox.showinfo(title=website, message= f'No details for {website} exists.')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = [random.choice(UPPER_CASES + LOWER_CASES) for _ in range(random.randint(8,10))] 
    password += [str(random.choice(NUMBERS)) for _ in range(random.randint(2,4))] 
    password += [random.choice(SYMBOLS) for _ in range(random.randint(2,4))]
    
    random.shuffle(password)
    password = "".join(password)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email_username,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Oops', message= "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail/Username: {email_username} \n' +
                                    f'Password: {password} \nIs it ok to save?')
        
        if is_ok:
            try:
                with open('data.json',mode='r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', mode= 'w') as data_file:
                    json.dump(new_data,data_file,indent=4)
            else: 
                data.update(new_data)
                with open('data.json', mode= 'w') as data_file:
                    json.dump(data,data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                email_username_entry.delete(0,END)
                email_username_entry.insert(0,DEFAULT_EMAIL)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

# Canvas
canvas = Canvas(width= 200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image = logo_image)
canvas.grid(row=0, column=1)

# Label
website_text = Label(text="Website:")
website_text.grid(row= 1,column=0)
email_username_text = Label(text="Email/Username:")
email_username_text.grid(row=2,column=0)
password_text = Label(text="Password:")
password_text.grid(row=3, column= 0)

# Entry
website_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_username_entry = Entry(width=38)
email_username_entry.grid(row=2,column=1,columnspan=2)
email_username_entry.insert(0,DEFAULT_EMAIL)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# Button
search_button = Button(text='Search', width=13, command= search_password)
search_button.grid(row=1,column=2)
generate_button = Button(text='Generate Password',width= 13,command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text='Add',width=36,command=save)
add_button.grid(row=4, column= 1,columnspan=2)


window.mainloop()