"""
pip install opencv-python mediapipe
"""

import cv2  # Импорт библиотеки OpenCV для работы с изображениями и видеопотоками
import mediapipe as mp  # Импорт библиотеки Mediapipe для распознавания рук

# Инициализация модуля Mediapipe Hands для обнаружения и отслеживания рук
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils  # Инструменты для визуализации ключевых точек и связей между ними


# Функция определения, выпрямлен ли большой палец
def is_thumb_extended(hand_landmarks, hand_handedness):
    # Получение информации о том, правая это рука или левая
    handedness = hand_handedness.classification[0].label

    # Получение координат кончика большого пальца и его MCP (метакарпофалангового соединения)
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]

    # Для правой руки выпрямленность определяется, если кончик пальца находится левее MCP, и наоборот для левой руки
    return thumb_tip.x < thumb_mcp.x if handedness == 'Right' else thumb_tip.x > thumb_mcp.x


# Функция подсчета выпрямленных пальцев
def count_extended_fingers(hand_landmarks, hand_handedness):
    extended_fingers = 0  # Счетчик выпрямленных пальцев

    # Проверка выпрямленности большого пальца
    if is_thumb_extended(hand_landmarks, hand_handedness):
        extended_fingers += 1

    # Проверка выпрямленности остальных пальцев
    for finger_tip_id in [8, 12, 16, 20]:  # Кончики указательного, среднего, безымянного и мизинца
        if hand_landmarks.landmark[finger_tip_id].y < hand_landmarks.landmark[finger_tip_id - 2].y:
            extended_fingers += 1  # Если кончик пальца выше (по Y), чем его PIP, палец считается выпрямленным

    return extended_fingers


# Начало захвата видео с веб-камеры
cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()  # Чтение кадра из видеопотока
    if not success:
        continue  # Пропуск пустых кадров

    # Подготовка изображения: переворот для создания зеркального отображения и конвертация в RGB
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)  # Обработка кадра с помощью Mediapipe

    # Конвертация обратно в BGR для отображения
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Если обнаружены руки, визуализация ключевых точек и подсчет выпрямленных пальцев
    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            extended_fingers = count_extended_fingers(hand_landmarks, handedness)
            # Вывод количества выпрямленных пальцев на изображение
            cv2.putText(image, f'Extended Fingers: {extended_fingers}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255), 2, cv2.LINE_AA)

    # Показать изображение в окне
    cv2.imshow('Hand Tracking', image)

    # Завершение цикла по нажатию клавиши Esc
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Освобождение ресурсов камеры и закрытие окон
cap.release()
cv2.destroyAllWindows()
