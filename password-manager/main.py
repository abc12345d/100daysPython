# import * only import classes and constants, but messagebox is a module
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

UPPER_CASES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWER_CASES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS = list(range(10))
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

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

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Oops', message= "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail/Username: {email_username} \n' +
                                    f'Password: {password} \nIs it ok to save?')
        
        if is_ok:
            with open('data.txt',mode='a') as file:
                record = f'{website} | {email_username} | {password}\n'
                file.write(record)

            website_entry.delete(0,END)
            password_entry.delete(0,END)

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
website_entry = Entry(width=38)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=38)
email_username_entry.grid(row=2,column=1,columnspan=2)
email_username_entry.insert(0,"abc@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# Button
generate_button = Button(text='Generate Password',width= 13,command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text='Add',width=36,command=save)
add_button.grid(row=4, column= 1,columnspan=2)


window.mainloop()