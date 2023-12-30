import random
import tkinter as tk

def generate_password():
    nr_letters = int(letters_entry.get())
    nr_symbols = int(symbols_entry.get())
    nr_numbers = int(numbers_entry.get())

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_display.config(text=f"Your password is: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x200")

# Labels
letters_label = tk.Label(root, text="How many letters would you like in your password?", font=("Arial", 12))
letters_label.pack()
letters_entry = tk.Entry(root, width=40, font=("Arial", 12))
letters_entry.pack()

symbols_label = tk.Label(root, text="How many symbols would you like?", font=("Arial", 12))
symbols_label.pack()
symbols_entry = tk.Entry(root, width=40, font=("Arial", 12))
symbols_entry.pack()

numbers_label = tk.Label(root, text="How many numbers would you like?", font=("Arial", 12))
numbers_label.pack()
numbers_entry = tk.Entry(root, width=40, font=("Arial", 12))
numbers_entry.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))
generate_button.pack()

# Display generated password
password_display = tk.Label(root, text="", font=("Arial", 14))
password_display.pack()

root.mainloop()
