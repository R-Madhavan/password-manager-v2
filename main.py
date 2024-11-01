from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator (mod from old project)
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json","r") as data_file:
                #Reading old data
                data = json.load(data_file)                         #read use "r"
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:               #write use "w"
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)                #write use "w"
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            try:
                data = json.load(data_file)
                print(data[website]["password"])
                messagebox.showinfo(title=website,message=f"Email: {data[website]["email"]} \npassword: {data[website]["password"]}.")
            except KeyError:
                messagebox.showinfo(title="Data not Found",message=f"No details for {website} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No Data File Found.")

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=50,pady=50)

#canvas
canvas = Canvas(height=200,width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entries
website_name = StringVar()
website_entry = Entry(width=30, textvariable=website_name)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()

email_name = StringVar()
email_entry = Entry(width=30, textvariable=email_name)
email_entry.grid(row=2,column=1,columnspan=1)
email_entry.insert(0, "example@gmail.com")

password_name = StringVar()
password_entry = Entry(width=30, textvariable=password_name)
password_entry.grid(row=3,column=1,columnspan=1)

#buttons
generate_button = Button(text="Generate Password", command=generate_password,width=15)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add",width=44,command=save)
add_button.grid(row=4, column=1,columnspan=2)
search_button = Button(text="Search", command=find_password,width=15)
search_button.grid(row=1,column=2)
windows.mainloop()
