import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# 1. Загрузка данных
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. Подготовка данных
# Нормализация (делим на 255, чтобы значения были в диапазоне от 0 до 1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# Преобразуем метки классов в формат one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 3. Построение нейронной сети
model = Sequential([
    Flatten(input_shape=(28, 28)),       # Преобразуем изображения 28x28 в одномерный массив
    Dense(128, activation='relu'),       # Первый полносвязный слой с 128 нейронами
    Dense(64, activation='relu'),        # Второй полносвязный слой с 64 нейронами
    Dense(10, activation='softmax')      # Выходной слой для 10 классов (цифры от 0 до 9)
])

# 4. Компиляция модели
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 5. Обучение модели
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))

# Оценка модели
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Точность на тестовых данных: {test_acc:.4f}')

# Сохранение модели в формате HDF5
model.save('mnist_digit_recognizer.h5')

