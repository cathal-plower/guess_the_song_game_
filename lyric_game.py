import tkinter as tk
from tkinter import messagebox
import random

# -----------------------------
# SONG DATABASE
# -----------------------------
SONGS = [
    {
        "lyric": "Started from the bottom, now we're here...",
        "answer": "Started From the Bottom",
        "options": ["Started From the Bottom", "God's Plan", "Energy", "Headlines"]
    },
    {
        "lyric": "You used to call me on my cell phone...",
        "answer": "Hotline Bling",
        "options": ["Hotline Bling", "One Dance", "Controlla", "Find Your Love"]
    },
    {
        "lyric": "I only love my bed and my momma, I'm sorry...",
        "answer": "God's Plan",
        "options": ["God's Plan", "Passionfruit", "Nice For What", "Energy"]
    },
    {
        "lyric": "Working on the weekend like usual...",
        "answer": "Nonstop",
        "options": ["Nonstop", "Mob Ties", "Jumpman", "Energy"]
    },
    {
        "lyric": "Know yourself, know your worth...",
        "answer": "Know Yourself",
        "options": ["Know Yourself", "Worst Behavior", "Legends", "Back To Back"]
    }
]

random.shuffle(SONGS)

current_question = 0
score = 0

# -----------------------------
# FUNCTIONS
# -----------------------------
def load_question():
    global current_question

    if current_question >= len(SONGS):
        end_game()
        return

    question = SONGS[current_question]

    question_label.config(
        text=f"Question {current_question + 1}/{len(SONGS)}"
    )

    lyric_label.config(
        text=question["lyric"]
    )

    options = question["options"].copy()
    random.shuffle(options)

    for i in range(4):
        buttons[i].config(
            text=options[i],
            command=lambda opt=options[i]: check_answer(opt)
        )


def check_answer(choice):
    global score, current_question

    correct_answer = SONGS[current_question]["answer"]

    if choice == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "✅ Correct Answer!")
    else:
        messagebox.showerror(
            "Incorrect",
            f"❌ Correct answer: {correct_answer}"
        )

    current_question += 1
    load_question()


def end_game():
    messagebox.showinfo(
        "Game Complete",
        f"Final Score: {score}/{len(SONGS)}"
    )

    root.destroy()


# -----------------------------
# WINDOW
# -----------------------------
root = tk.Tk()
root.title("Lyric Guessing Game")
root.geometry("700x500")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="🎵 Lyric Guessing Game 🎵",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=20)

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    fg="white",
    bg="#1e1e1e"
)
question_label.pack()

lyric_label = tk.Label(
    root,
    text="",
    font=("Arial", 18),
    fg="cyan",
    bg="#1e1e1e",
    wraplength=600
)
lyric_label.pack(pady=30)

buttons = []

for _ in range(4):
    btn = tk.Button(
        root,
        width=40,
        height=2,
        font=("Arial", 12)
    )
    btn.pack(pady=5)
    buttons.append(btn)

score_label = tk.Label(
    root,
    text="Guess the song!",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e1e"
)
score_label.pack(pady=20)

load_question()

root.mainloop()