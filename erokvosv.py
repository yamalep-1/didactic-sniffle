import tkinter as tk
from tkinter import messagebox
import random

def start_game():
    try:
        limit = int(entry_limit.get())
        if limit <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введи положительное целое число для диапазона!")
        return

    global secret_number, attempts
    secret_number = random.randint(-limit, limit)
    attempts = 0
    result_label.config(text=f"🎲 Я загадал число от {-limit} до {limit}. Угадай!", fg="#FF6EC7")
    entry_guess.delete(0, tk.END)
    entry_guess.focus()

def check_guess(event=None):
    global attempts
    try:
        guess = int(entry_guess.get())
    except ValueError:
        messagebox.showwarning("Внимание", "Вводи только целые числа!")
        entry_guess.delete(0, tk.END)
        return

    attempts += 1

    if guess == secret_number:
        result_label.config(
            text=f"🎉 Ура! Ты угадал число {secret_number} за {attempts} попыток!",
            fg="#00FFD1"
        )
        messagebox.showinfo("Победа", f"Ты угадал число {secret_number} за {attempts} попыток!")
    elif guess < secret_number:
        result_label.config(
            text="📈 Моё число больше. \nИди уроки делай, дебил!",
            fg="#FF3E6C"
        )
    else:
        result_label.config(
            text="📉 Моё число меньше. \nИди уроки делай, дебил!",
            fg="#FF3E6C"
        )

    entry_guess.delete(0, tk.END)
    entry_guess.focus()

# === Создаём окно ===
root = tk.Tk()
root.title("🔮 Угадай число")
root.geometry("450x420")
root.configure(bg="#1A0B2E")  # Глубокий тёмно-фиолетовый

# === Стили кнопок ===
btn_style_start = {
    "bg": "#FF3E9D",        # Неоновый розовый
    "fg": "#FFFFFF",
    "activebackground": "#FF6EC7",
    "activeforeground": "#FFFFFF",
    "font": ("Arial", 12, "bold"),
    "relief": "flat",
    "bd": 0,
    "padx": 20,
    "pady": 8,
    "cursor": "hand2"
}

btn_style_check = {
    "bg": "#00D9FF",        # Неоновый голубой
    "fg": "#1A0B2E",
    "activebackground": "#00FFD1",
    "activeforeground": "#1A0B2E",
    "font": ("Arial", 12, "bold"),
    "relief": "flat",
    "bd": 0,
    "padx": 20,
    "pady": 8,
    "cursor": "hand2"
}

label_style = {
    "bg": "#1A0B2E",
    "fg": "#D9B8FF",
    "font": ("Arial", 11)
}

entry_style = {
    "bg": "#2D1B4E",
    "fg": "#FFFFFF",
    "insertbackground": "#FF6EC7",
    "font": ("Arial", 12),
    "relief": "flat",
    "bd": 2
}

# === Поле для задания диапазона ===
tk.Label(root, text="Введи предел диапазона (например, 50 → от -50 до 50):",
         **label_style).pack(pady=(15, 5))

entry_limit = tk.Entry(root, width=22, **entry_style)
entry_limit.pack(pady=5, ipady=5)

# === Кнопка старта ===
btn_start = tk.Button(root, text="🎮 Начать игру", command=start_game, **btn_style_start)
btn_start.pack(pady=12)

# === Поле для ввода догадки ===
tk.Label(root, text="Твоя догадка:", **label_style).pack(pady=(10, 5))

entry_guess = tk.Entry(root, width=22, **entry_style)
entry_guess.pack(pady=5, ipady=5)
# Enter тоже проверяет догадку
entry_guess.bind("<Return>", check_guess)

# === Кнопка проверки ===
btn_check = tk.Button(root, text="✨ Проверить", command=check_guess, **btn_style_check)
btn_check.pack(pady=10)

# === Поле для результата ===
result_label = tk.Label(root, text="Задай диапазон и нажми 'Начать игру'",
                        bg="#1A0B2E", fg="#A988D8",
                        font=("Arial", 12, "bold"), wraplength=400)
result_label.pack(pady=15)

# === Hover-эффекты для кнопок ===
def on_enter(e, btn, color):
    btn["bg"] = color
def on_leave(e, btn, color):
    btn["bg"] = color

btn_start.bind("<Enter>", lambda e: btn_start.config(bg="#FF6EC7"))
btn_start.bind("<Leave>", lambda e: btn_start.config(bg="#FF3E9D"))
btn_check.bind("<Enter>", lambda e: btn_check.config(bg="#00FFD1"))
btn_check.bind("<Leave>", lambda e: btn_check.config(bg="#00D9FF"))

root.mainloop()