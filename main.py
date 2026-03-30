import tkinter as tk
from PIL import Image, ImageTk
import random

# ---------------- SCORE ---------------- #
user_score = 0
comp_score = 0

# ---------------- FUNCTION ---------------- #
def play(user_choice):
    global user_score, comp_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    user_label.config(text="You: " + user_choice)
    comp_label.config(text="Computer: " + computer_choice)

    # Game logic
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        comp_score += 1

    result_label.config(text=result)

    # Update Scoreboard
    score_label.config(text=f"Score → You: {user_score} | Computer: {comp_score}")

# ---------------- GUI SETUP ---------------- #
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x500")
root.config(bg="#e6f2ff")

title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 20, "bold"), bg="#e6f2ff")
title.pack(pady=10)

# Scoreboard
score_label = tk.Label(root, text="Score → You: 0 | Computer: 0",
font=("Arial", 14, "bold"), fg="green", bg="#e6f2ff")
score_label.pack(pady=10)

# Result Labels
user_label = tk.Label(root, text="You: ", font=("Arial", 12), bg="#e6f2ff")
user_label.pack()

comp_label = tk.Label(root, text="Computer: ", font=("Arial", 12), bg="#e6f2ff")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="blue", bg="#e6f2ff")
result_label.pack(pady=20)

# ---------------- LOAD IMAGES ---------------- #
def load_image(path):
    img = Image.open(path)
    img = img.resize((100, 100))
    return ImageTk.PhotoImage(img)

rock_img = load_image("rock.png")
paper_img = load_image("paper.png")
scissor_img = load_image("scissors.png")

# ---------------- BUTTONS ---------------- #
frame = tk.Frame(root, bg="#e6f2ff")
frame.pack(pady=20)

rock_btn = tk.Button(frame, image=rock_img, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(frame, image=paper_img, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissor_btn = tk.Button(frame, image=scissor_img, command=lambda: play("Scissors"))
scissor_btn.grid(row=0, column=2, padx=10)

# Exit Button
exit_btn = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white")
exit_btn.pack(pady=10)

# Run App
root.mainloop()