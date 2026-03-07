from tkinter import *
import time

window = Tk()
window.title("Typing Speed Test")
window.geometry("1000x700")
window.config(bg="#1e293b")

def start_test():
    window.start_time = time.time()
    typing_box.delete("1.0", END)

def check_speed():
    end_time = time.time()
    time_taken = end_time - window.start_time
    minutes = time_taken / 60
    user_text = typing_box.get("1.0", END).strip()
    words = len(user_text.split())
    wpm = int(words / minutes)

    sample_words = sample_text.lower().split()
    typed_words = user_text.lower().split()

    correct_words = 0
    for i in range(min(len(sample_words), len(typed_words))):
        if sample_words[i] == typed_words[i]:
            correct_words += 1

    accuracy = (correct_words / len(sample_words)) * 100
    result_label.config(text=f"Typing speed: {wpm} WPM | Accuracy: {int(accuracy)}%")



sample_text = """
Learning to type quickly is an important skill in today's digital world. 
Programmers, writers, and students spend many hours working on computers. 
Improving your typing speed can help you complete tasks faster and become 
more productive. With regular practice and focus on accuracy, anyone can 
increase their typing speed and confidence over time.
"""

title = Label(window, text="Typing Speed Test", font=("Arial", 24, "bold"), fg="#f8fafc", bg="#1e293b")
title.pack(pady=20)

text_label = Label(window, text=sample_text, wraplength=850, font=("Arial", 16), justify="center",  fg="#f8fafc",
    bg="#1e293b")
text_label.pack(pady=40)

typing_box = Text(window, height=8, width=80, font=("Arial", 14), bg="#334155", fg="#f8fafc", insertbackground="white")
typing_box.pack(pady=20)

start_button = Button(window, text="Start Test", font=("Arial", 14), bg="#3b82f6", fg="white", padx=20, pady=5, command=start_test)
start_button.pack(pady=10)

check_button = Button(window, text="Check Speed", font=("Arial", 14), bg="#3b82f6", fg="white", padx=20, pady=5, command=check_speed)
check_button.pack(pady=10)

result_label = Label(window, text="Typing Speed: 0 WPM", font=("Arial", 16), fg="#f8fafc", bg="#1e293b")
result_label.pack(pady=20)

window.mainloop()