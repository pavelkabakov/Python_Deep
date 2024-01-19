import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download()
        messagebox.showinfo("Успех", "Видео успешно загружено")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Создание окна
root = tk.Tk()
root.title("Загрузчик видео с YouTube")

# Создание виджетов
url_label = tk.Label(root, text="Введите URL видео:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Загрузить видео", command=download_video)
download_button.pack()

# Запуск цикла обработки событий
root.mainloop()
