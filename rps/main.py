from tkinter import *
from tkinter import PhotoImage
import random

BG = "#9DBC98"
FG = "black"

def on_rock():
    global player_score, pc_score
    op = random.randint(0, 2)
    result = get_result(op, 0)  # 0 corresponds to rock
    display_result(result)
    update_scores(result)

def on_paper():
    global player_score, pc_score
    op = random.randint(0, 2)
    result = get_result(op, 1)  # 1 corresponds to paper
    display_result(result)
    update_scores(result)

def on_scissors():
    global player_score, pc_score
    op = random.randint(0, 2)
    result = get_result(op, 2)  # 2 corresponds to scissors
    display_result(result)
    update_scores(result)

def get_result(opponent_choice, player_choice):
    if opponent_choice == player_choice:
        return "Tie"
    elif (opponent_choice + 1) % 3 == player_choice:
        return "Player wins"
    else:
        return "PC wins"

def update_scores(result):
    global player_score, pc_score
    if result == "Player wins":
        player_score += 1
    elif result == "PC wins":
        pc_score += 1
    player_score_label.config(text=f"Player: {player_score}")
    pc_score_label.config(text=f"PC: {pc_score}")

def display_result(result):
    result_label.config(text=result)
    root.after(3000, clear_result)

def clear_result():
    result_label.config(text="")

player_score = 0
pc_score = 0

desired_width = 200
desired_height = 200

root = Tk()
root.title("rock-paper-scissors")
root.configure(bg=BG)

rock_image = PhotoImage(file="rock.png")
paper_image = PhotoImage(file="paper.png")
scissors_image = PhotoImage(file="scissors.png")
images = [rock_image, paper_image, scissors_image]
i = []
for image in images:
    i.append(image.subsample(image.width() // desired_width, image.height() // desired_height))

label = Label(text="Rock Paper Scissors", font=("Arial", 24, "bold"), bg=BG, borderwidth=0, pady=30)
label.grid(column=1, row=0)

player_score_label = Label(text=f"Player: {player_score}", font=("Arial", 24, "bold"), bg=BG, borderwidth=0, padx=20)
player_score_label.grid(column=0, row=1)

pc_score_label = Label(text=f"PC: {pc_score}", font=("Arial", 24, "bold"), bg=BG, borderwidth=0, padx=20)
pc_score_label.grid(column=2, row=1)

rock_button = Button(root, text="ROCK", image=i[0], command=on_rock, bg=BG, borderwidth=0, padx=50, pady=30)
rock_button.grid(column=0, row=2)

paper_button = Button(root, text="PAPER", image=i[1], command=on_paper, bg=BG, borderwidth=0, padx=50, pady=30)
paper_button.grid(column=1, row=2)

scissors_button = Button(root, text="SCISSORS", image=i[2], command=on_scissors, bg=BG, borderwidth=0, padx=50, pady=30)
scissors_button.grid(column=2, row=2)

result_label = Label(root, text="", font=("Arial", 16), bg=BG)
result_label.grid(column=1, row=3)

root.mainloop()
