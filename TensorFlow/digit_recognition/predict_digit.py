import numpy as np
from PIL import Image, ImageTk
import tensorflow as tf
import tkinter as tk
from tkinter import filedialog, Label, Button
import sys
import io

# Установка кодировки для стандартного вывода
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Загружаем обученную модель
model = tf.keras.models.load_model('mnist_digit_recognizer.h5')

# Функция для загрузки и предобработки изображения
def load_and_preprocess_image(image_path):
    img = Image.open(image_path).convert('L')  # Преобразуем в оттенки серого
    img = img.resize((28, 28))                 # Изменение размера до 28x28 пикселей
    img_array = np.array(img) / 255.0          # Нормализация значений пикселей
    img_array = 1 - img_array                  # Инвертируем цвета, если фон белый
    img_array = img_array.reshape((1, 28, 28)) # Подготавливаем форму для модели
    return img_array

# Функция для выбора файла и распознавания цифры
def recognize_digit():
    # Открываем диалог выбора файла
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return  # Если файл не выбран, выходим из функции

    # Загружаем и подготавливаем изображение для модели
    img_array = load_and_preprocess_image(image_path)
    predictions = model.predict(img_array)
    predicted_digit = np.argmax(predictions)  # Определяем цифру с наибольшей вероятностью

    # Отображаем миниатюру изображения
    img = Image.open(image_path)
    img.thumbnail((150, 150))  # Уменьшаем изображение для отображения в окне
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk  # Сохраняем ссылку на изображение, чтобы избежать его удаления

    # Отображаем результат распознавания
    result_label.config(text=f'Распознанная цифра: {predicted_digit}')

# Создаем основное окно приложения
root = tk.Tk()
root.title("Распознавание цифр")

# Кнопка для выбора изображения
choose_button = Button(root, text="Выбрать изображение", command=recognize_digit)
choose_button.pack(pady=10)

# Метка для отображения миниатюры изображения
image_label = Label(root)
image_label.pack(pady=10)

# Метка для отображения результата распознавания
result_label = Label(root, text="Распознанная цифра: ")
result_label.pack(pady=10)

# Запускаем основной цикл приложения
root.mainloop()
