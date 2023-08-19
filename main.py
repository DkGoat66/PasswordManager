import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


# ------------------------find_password--------------------------------------------#
def find_password():
    website = website_blank.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="NO Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email:{email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    Password_blank.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_blank.get()
    email = Email_UserNameBlank.get()
    password = Password_blank.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any filed empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "  w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_blank.delete(0, END)
            Password_blank.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
Email_UserName = Label(text="Email/Username:")
Email_UserName.grid(row=2, column=0)
Password = Label(text="Password")
Password.grid(row=3, column=0)

website_blank = Entry(width=21)
website_blank.grid(row=1, column=1)
website_blank.focus()
Email_UserNameBlank = Entry(width=35)
Email_UserNameBlank.grid(row=2, column=1, columnspan=2)
Email_UserNameBlank.insert(0, "DK@gmail.com")
Password_blank = Entry(width=21)
Password_blank.grid(row=3, column=1)


search_image=PhotoImage(file="icons8-search-48.png")
search_button = Button(image=search_image, width=13, command=find_password)
search_button.grid(row=1, column=2)
Generate_Password_button = Button(text="Generate Password", command=generate_password)
Generate_Password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
