import numpy as np
from PIL import Image
import tensorflow as tf
import sys
import io

# Установка кодировки для стандартного вывода в UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Загрузка сохраненной модели
model = tf.keras.models.load_model('mnist_digit_recognizer.h5')


# Функция для загрузки и предобработки изображения
def load_and_preprocess_image(image_path):
    img = Image.open(image_path).convert('L')  # Преобразование в оттенки серого
    img = img.resize((28, 28))  # Изменение размера на 28x28
    img_array = np.array(img) / 255.0  # Нормализация
    img_array = 1 - img_array  # Инвертирование цветов (если фон белый)
    img_array = img_array.reshape((1, 28, 28))  # Преобразование для подачи в модель

    return img_array


# Путь к вашему изображению
image_path = '1.png'

# Загрузка и предобработка изображения
img_array = load_and_preprocess_image(image_path)

# Использование модели для предсказания
predictions = model.predict(img_array)
predicted_digit = np.argmax(predictions)

print(f'Распознанная цифра: {predicted_digit}')
