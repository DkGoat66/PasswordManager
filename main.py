import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

# ------------------------ PASSWORD SEARCH FUNCTION -------------------------------#
# Function to find and display the password for a given website
def find_password():
    website = website_blank.get()  # Get the website name from the input field
    try:
        with open("data.json") as data_file:  # Attempt to open the data file
            data = json.load(data_file)  # Load the JSON data
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")  # Show error if file not found
    else:
        if website in data:  # Check if the website exists in the data
            email = data[website]["email"]  # Extract email
            password = data[website]["password"]  # Extract password
            # Display the email and password
            messagebox.showinfo(title=website, message=f"email:{email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")  # Show error if website not found

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Function to generate and display a random password
def generate_password():
    # Define possible characters for the password
    letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    numbers = [str(i) for i in range(0, 10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate parts of the password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine and shuffle to finalize the password
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    # Display the password and copy it to the clipboard
    Password_blank.insert(0, password)
    pyperclip.copy(password)
    # ---------------------------- SAVE PASSWORD FUNCTION ------------------------------- #
# Function to save the website, email, and password details to a file
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

    # Ensure no fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Create a new file if it doesn't exist
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Save updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear the input fields
            website_blank.delete(0, END)
            Password_blank.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
# Setup the GUI for the application
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Add and position the canvas and logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Define and place the labels and entry fields for the website, email/username, and password
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
Email_UserNameBlank.grid(row=





