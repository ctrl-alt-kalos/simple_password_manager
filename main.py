from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Oops", message=f"No Data File Found.")
    else:
        if website in data.keys():
            messagebox.showinfo(title=f"{website}", message=f"Username/Email: {data[website]['user']}\n"
                                                            f"Password: {data[website]['password']}\n"
                                                            f"(Click \"ok\" to save password to the clipboard)")
            pyperclip.copy(data[website]['password'])
        else:
            messagebox.showinfo(title=f"Oops", message=f"No details for the website {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list_1 = [choice(letters) for char in range(randint(8, 10))]
    password_list_2 = [choice(symbols) for char in range(randint(2, 4))]
    password_list_3 = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_list_3 + password_list_2 + password_list_1
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def clicked_add():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "user": user,
            "password": password
        }
    }

    if len(website) != 0 and len(user) != 0 and len(password) != 0:
        try:
            with open("data.json", 'r') as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # creating new json file
                json.dump(new_data, data_file, indent=4)
        else:
            # updating with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Olac Password Manager")
window.maxsize(width=520, height=400)
window.minsize(width=520, height=400)
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="olac.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=clicked_add)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

# Enteries
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()

user_entry = Entry(width=53)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "user@mail.com")

password_entry = Entry(width=34)     # show="*"
password_entry.grid(row=3, column=1)

window.mainloop()
