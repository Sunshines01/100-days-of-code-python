# Password manager - Complete on Day 30

A simple, secure, and lightweight password manager built in Python that helps you generate strong passwords, store them locally, and retrieve them when needed — all without relying on third-party services.

## Concepts practised:
- Catching exceptions
- Raising exceptions
- Read, write and update JSON data
- Working with images
- Setting up a user interface
- Saving data to file
- Dialog boxes and pop-ups in tkinter
- Using pyperclip

## Features

- **Generate Strong Passwords**: Automatically creates cryptographically secure passwords with customizable length and character sets (uppercase, lowercase, digits, symbols).
- **Copy to Clipboard**: Generated passwords are instantly copied to your clipboard for easy pasting — no need to expose sensitive data on screen.
- **Local Storage**: All credentials (website, username/email, and password) are stored securely on your local machine using encrypted storage.
- **Search by Website**: Quickly retrieve saved login information by entering the name of the website.
- **Secure & Private**: No data is sent over the internet. Everything stays on your device.

## How to Use

1. **Save a New Password**  
   Run the script and choose to generate a password. Enter the website name and your email. The app will generate a strong password, save it encrypted, and copy it to your clipboard.

2. **Retrieve a Password**  
   Select the search option and enter the name of the website. The stored email and password will be decrypted and displayed (or the password will be copied to clipboard for security).
