"""
pip install opencv-python mediapipe
"""

import cv2
import mediapipe as mp

# Инициализация Mediapipe для обнаружения рук
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils


def is_thumb_extended(hand_landmarks, hand_handedness):
    # Определение направленности руки
    handedness = hand_handedness.classification[0].label

    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]

    # Для правой руки
    if handedness == 'Right':
        return thumb_tip.x < thumb_mcp.x
    # Для левой руки
    else:
        return thumb_tip.x > thumb_mcp.x


def count_extended_fingers(hand_landmarks, hand_handedness):
    extended_fingers = 0

    # Проверка большого пальца
    if is_thumb_extended(hand_landmarks, hand_handedness):
        extended_fingers += 1

    # Проверка остальных пальцев
    for finger_tip_id in [8, 12, 16, 20]:  # Индексы кончиков пальцев
        if hand_landmarks.landmark[finger_tip_id].y < hand_landmarks.landmark[finger_tip_id - 2].y:
            extended_fingers += 1

    return extended_fingers


cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    if not success:
        continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Подсчет выпрямленных пальцев
            extended_fingers = count_extended_fingers(hand_landmarks, handedness)

            # Отображение количества выпрямленных пальцев
            cv2.putText(image, f'Extended Fingers: {extended_fingers}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Hand Tracking', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
