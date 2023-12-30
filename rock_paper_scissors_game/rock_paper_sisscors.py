import random
import tkinter as tk
from PIL import Image, ImageTk

def play_game(user_choice):
    games_edges = ["Rock", "Paper", "Scissors"]
    computer_choice = random.randint(0, 2)

    user_display.config(text=f"Your choice: {games_edges[user_choice]}", fg="blue")
    computer_display.config(text=f"Computer choice: {games_edges[computer_choice]}", fg="red")

    if user_choice >= 3 or user_choice < 0:
        result_display.config(text="You typed an invalid number", fg="black")
    else:
        result = ""
        if user_choice == computer_choice:
            result = "It's a draw!"
        elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
            result = "You win!"
            update_user_score()
        else:
            result = "You lose!"
            update_comp_score()
        
        result_display.config(text=result, fg="green")


# update user score
def update_user_score():
    score = int(user_Score["text"])
    score += 1
    user_Score["text"] = str(score)


# update computer score
def update_comp_score():
    score = int(computer_Score["text"])
    score += 1
    computer_Score["text"] = str(score)

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("670x350")
root.resizable(False, False)

button_style = {"padx": 10, "pady": 10}

# Load images for Rock, Paper, and Scissors
rock_img = Image.open("rock.png")
paper_img = Image.open("paper.png")
scissors_img = Image.open("scissors.png")


# Convert images to Tkinter PhotoImage
rock_photo = ImageTk.PhotoImage(rock_img)
paper_photo = ImageTk.PhotoImage(paper_img)
scissors_photo = ImageTk.PhotoImage(scissors_img)

# Rock button
rock_button = tk.Button(root, image=rock_photo, command=lambda: play_game(0), **button_style).grid(row=2, column=0)

# Paper button
paper_button = tk.Button(root, image=paper_photo, command=lambda: play_game(1), **button_style).grid(row=2, column=1)


# Scissors button
scissors_button = tk.Button(root, image=scissors_photo, command=lambda: play_game(2), **button_style).grid(row=2, column=2)

# User display label
user_display = tk.Label(root, text="Your choice:", fg="blue", font=("Helvetica", 15))
user_display.grid(row=0, column=0)

# scores
user_Score = tk.Label(root, text=0, font=("Helvetica", 36), fg="blue")
computer_Score = tk.Label(root, text=0, font=("Helvetica", 36), fg="red")
computer_Score.grid(row=1, column=2)
user_Score.grid(row=1, column=0)


# Computer display label
computer_display = tk.Label(root, text="Computer choice:", fg="red",font=("Helvetica", 15))
computer_display.grid(row=0, column=2)

# Result display label
result_display = tk.Label(root, text="Result Update", fg="green",font=("Helvetica", 15))
result_display.grid(row=0, column=1)

root.mainloop()


