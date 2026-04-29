import tkinter as tk
import random
from locale import windows_locale

# Переменная с ссылкой на GitHub‑репозиторий
git_hub = "https://github.com/ваш_логин/ваш_репозиторий"

# Список интересных фактов
facts = [
    "Бананы радиоактивны и излучают небольшое количество гамма‑излучения.",
    "Человек может обойтись без пищи до 2 месяцев, а без воды — всего несколько дней.",
    "Голубые киты ежедневно потребляют около 4 тонн пищи.",
    "Пчёлы могут распознавать лица людей.",
    "Существует 6 000 видов бананов, а не только один."
]

def show_random_fact():
    """Функция для выбора и отображения случайного факта."""
    random_fact = random.choice(facts)
    fact_label.config(text=random_fact)

# Создание главного окна приложения
windows_locale = tk.Tk()
windows_locale.title("Случайный интересный факт")
windows_locale.geometry("500x200")  # Задаём размер окна
windows_locale.resizable(False, False)  # Запрещаем изменение размера окна

# Создание метки для вывода факта
fact_label = tk.Label(
    windows_locale,
    text="Нажмите кнопку, чтобы узнать интересный факт!",
    wraplength=480,  # Перенос текста, если он не помещается в ширину
    justify="center",  # Выравнивание текста по центру
    font=("Arial", 12)
)
fact_label.pack(pady=20)  # Размещаем метку с отступом сверху и снизу

# Создание кнопки «Показать факт»
show_fact_button = tk.Button(
    windows_locale,
    text="Показать факт",
    command=show_random_fact,  # Привязываем функцию к событию нажатия
    font=("Arial", 14),
    bg="#4CAF50",  # Зелёный фон кнопки
    fg="white",  # Белый цвет текста
    padx=20,
    pady=10
)
show_fact_button.pack(pady=10)  # Размещаем кнопку с отступом

# Запуск главного цикла приложения
windows_locale.mainloop()