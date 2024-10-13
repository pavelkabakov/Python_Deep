import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube


def show_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_bar['value'] = percentage_of_completion
    root.update_idletasks()


def download_video():
    folder = filedialog.askdirectory()
    if not folder:
        return

    url = url_entry.get()
    try:
        yt = YouTube(url, on_progress_callback=show_progress)
        yt.streams.get_highest_resolution().download(output_path=folder)
        messagebox.showinfo("Успех", "Видео успешно загружено")
        progress_bar['value'] = 0  # сброс полосы прогресса после загрузки
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

progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack()

# Запуск цикла обработки событий
root.mainloop()
