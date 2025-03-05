import json
import os
import base64
from random import choice, randint, shuffle
import tkinter as tk
from tkinter import messagebox, simpledialog
import pyperclip
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        # Setup paths
        self.DATA_FILE = "data.json"
        self.KEY_FILE = "secret.key"
        
        # Initialize encryption
        self.setup_encryption()
        
        # Create UI
        self.create_ui()

    def setup_encryption(self):
        """Initialize or load encryption key"""
        if not os.path.exists(self.KEY_FILE):
            key = Fernet.generate_key()
            with open(self.KEY_FILE, 'wb') as key_file:
                key_file.write(key)
        
        with open(self.KEY_FILE, 'rb') as key_file:
            self.encryption_key = key_file.read()
        
        self.cipher_suite = Fernet(self.encryption_key)

    def encrypt_password(self, password):
        """Encrypt a password"""
        return self.cipher_suite.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        """Decrypt a password"""
        return self.cipher_suite.decrypt(encrypted_password.encode()).decode()

    def create_ui(self):
        """Create the main application UI"""
        self.window = tk.Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)

        # Logo
        self.canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
        self.logo_img = tk.PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)

        # Labels
        tk.Label(text="Website:").grid(row=1, column=0)
        tk.Label(text="Email/Username:").grid(row=2, column=0)
        tk.Label(text="Password:").grid(row=3, column=0)

        # Entry Fields
        self.website_entry = tk.Entry(width=21)
        self.website_entry.grid(row=1, column=1)
        self.website_entry.focus()

        self.email_entry = tk.Entry(width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        
        self.password_entry = tk.Entry(width=21)
        self.password_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(text="Search", command=self.find_password).grid(row=1, column=2)
        tk.Button(text="Generate Password", command=self.generate_password).grid(row=3, column=2)
        tk.Button(text="Add", command=self.save_password).grid(row=4, column=1, columnspan=2)

        self.window.mainloop()

    def generate_password(self):
        """Generate a strong random password"""
        letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        numbers = [str(i) for i in range(0, 10)]
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)
        password = "".join(password_list)

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo(title="Password Generated", message="Password copied to clipboard!")

    def save_password(self):
        """Save website credentials to JSON file"""
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Validate input
        if not website or not email or not password:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields.")
            return

        # Encrypt the password
        encrypted_password = self.encrypt_password(password)

        new_data = {
            website: {
                "email": email,
                "password": encrypted_password
            }
        }

        try:
            # Read existing data or create new file
            with open(self.DATA_FILE, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}

        # Update data
        data.update(new_data)

        # Save updated data
        with open(self.DATA_FILE, "w") as data_file:
            json.dump(data, data_file, indent=4)

        # Clear entries
        self.website_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Password saved successfully!")

    def find_password(self):
        """Find and display password for a website"""
        website = self.website_entry.get()

        try:
            with open(self.DATA_FILE, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No data file found.")
            return

        if website in data:
            email = data[website]["email"]
            encrypted_password = data[website]["password"]
            
            # Decrypt the password
            try:
                decrypted_password = self.decrypt_password(encrypted_password)
                
                # Option to copy password
                copy_password = messagebox.askyesno(
                    "Password Found", 
                    f"Email: {email}\n\nWould you like to copy the password to clipboard?"
                )
                
                if copy_password:
                    pyperclip.copy(decrypted_password)
                    messagebox.showinfo("Copied", "Password copied to clipboard!")
            
            except Exception as e:
                messagebox.showerror("Decryption Error", "Could not decrypt the password.")
        else:
            messagebox.showinfo("Not Found", f"No details for {website} exist.")

def main():
    print("Starting Password Manager...")
    PasswordManager()

if __name__ == "__main__":
    main()
