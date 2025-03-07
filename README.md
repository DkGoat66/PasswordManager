# Password Manager

## Overview

The Password Manager is a Python-based application that securely stores, generates, and retrieves passwords for various websites. It features a graphical user interface (GUI) built using Tkinter and stores credentials in a JSON file. The application includes functionality to search for saved passwords, generate strong random passwords, and securely store login credentials.

## Features

**Password Search**: Retrieve stored credentials for a given website.

**Password Generator**: Generate secure passwords with letters, numbers, and symbols.

**Save Credentials**: Store website, email/username, and password details in a JSON file.

**Clipboard Copy**: Automatically copy generated passwords to the clipboard.

**User-friendly Interface**: Simple GUI for easy interaction.

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from Python's official website.

### Required Libraries

Install the required dependencies by running:

`pip install pyperclip`

## Usage

1. Run the application:


`python password_manager.py`

2. To save a password:
 - Enter the website name.
 - Enter the email/username.
 - Click on "Generate Password" (or enter your password).
 - Click "Add" to save the credentials.

3. To search for a password:

- Enter the website name in the search field.
- Click "Search" to retrieve stored credentials.

File Structure

password_manager.py - The main script that runs the application.

data.json - Stores saved credentials in JSON format.

logo.png - Application logo used in the UI.

