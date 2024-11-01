# password-manager-v2
This is an updated version password manager application built using Python and Tkinter. This application allows you to generate secure passwords, save login details for websites, and search for saved credentials.

## Features

- **Password Generator**: Generates random, strong passwords with a combination of letters, numbers, and symbols.
- **Save Credentials**: Saves website name, email/username, and password to a JSON file.
- **Clipboard Copy**: Automatically copies the generated password to the clipboard.

## New Feature
- **Find Credentials**: Searches for saved login details for a website, using search button.

## Installation

### Requirements

- Python 3.x
- Required libraries:
  - `tkinter`
  - `pyperclip`

To install `pyperclip`, use:

```bash
pip install pyperclip
```

### Setup

1. Clone the repository or download the source code.
2. Place an image named `logo.png` in the project folder for the logo.

## Usage

Run the application with:

```bash
python main.py
```

### User Interface

- **Website**: Enter the website name (required for saving or searching credentials).
- **Email/Username**: Enter the email or username associated with the account (can be customized).
- **Password**: Displays the generated password. You can also manually enter a password.
  
#### Buttons

- **Generate Password**: Generates a strong password and copies it to the clipboard.
- **Add**: Saves the entered website, email, and password details to `data.json`.
- **Search**: Searches for credentials of the specified website in `data.json`.

### File Structure

- **main.py**: The main file containing all the code.
- **data.json**: The file where credentials are saved in JSON format.
- **data.json**: The data's are stored in this file (you can delete it completely, while running the program it creates new file if the data_file doesn't exist.  

### Error Handling

- **FileNotFoundError**: If `data.json` is not found, it creates a new file.
- **KeyError**: If credentials for the searched website are not found, it displays a message.

## JSON Data Format

The credentials are saved in a `data.json` file with the following structure:

```json
{
    "example.com": {
        "email": "user@example.com",
        "password": "generated_password"
    },
    ...
}
```

## Screenshots

![image](https://github.com/user-attachments/assets/fec0f066-e446-4da7-9d27-3fb54bff1654)
