# С начала суток прошло N секунд (N – целое). Найти количество полных минут, прошедших с начала последнего часа.
import tkinter as tk
from tkinter import messagebox


def calculate_minutes():
    try:
        n = int(entry.get())
        minutes = (n // 60) % 60
        result_label.config(text=f'Количество полных минут: {minutes}')
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное количество секунд.")


root = tk.Tk()
root.title("Калькулятор минут")
root.geometry('300x300+400+100')

entry_label = tk.Label(root, text="Введите количество секунд:")
entry_label.place(relx=0.25, rely=0.05)

entry = tk.Entry(root)
entry.place(relx=0.3, rely=0.15)

calc_button = tk.Button(root, text="Рассчитать", command=calculate_minutes)
calc_button.place(relx=0.38, rely=0.25)

result_label = tk.Label(root, text="Количество полных минут: ")
result_label.place(relx=0.2, rely=0.45)

root.mainloop()
