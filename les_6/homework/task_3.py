"""
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
варианты и выведите 4 успешных расстановки.

Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
 в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся на одной
  вертикали, горизонтали или диагонали.

Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.

Пример использования На входе:
print(generate_boards())
На выходе:
[[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)], [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)], [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)], [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]

"""

from random import shuffle


def is_attacking(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


def generate_boards():
    board_list = []
    attempts = 0
    while len(board_list) < 4:
        # Генерируем случайную расстановку ферзей
        rows = list(range(1, 9))  # Ряды от 1 до 8
        cols = list(range(1, 9))  # Колонки от 1 до 8
        shuffle(cols)  # Перемешиваем колонки для генерации случайной расстановки
        queens = list(zip(rows, cols))

        if check_queens(queens):
            board_list.append(queens)
        attempts += 1
        if attempts > 10000:
            break  # Безопасный выход из потенциального бесконечного цикла
    return board_list


# Генерируем и сохраняем 4 успешных расстановки
# board_list = generate_boards()

# Пример вывода для проверки
# for board in board_list:  # Печатаем только первую расстановку для примера
#     print(board)

print(generate_boards())