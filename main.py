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

