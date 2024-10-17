import heapq

# Функция для вычисления манхэттенского расстояния между двумя точками
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def astar(grid, start, goal):
    # Инициализация словарей для хранения стоимостей и предыдущих точек
    cost = {start: 0}
    came_from = {start: None}

    # Приоритетная очередь для хранения точек и их оценок (приоритетов)
    priority_queue = [(0, start)]

    while priority_queue:
        # Извлечение точки с минимальной оценкой
        current_cost, current_point = heapq.heappop(priority_queue)

        # Если достигнута целевая точка, завершаем алгоритм
        if current_point == goal:
            break

        # Рассмотрение соседних точек
        for neighbor in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current_point[0] + neighbor[0], current_point[1] + neighbor[1]

            new_cost = cost[current_point] + 1  # Стоимость перемещения на одну ячейку

            # Проверка на наличие препятствия и обновление стоимости, если новый путь короче
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                if (x, y) not in cost or new_cost < cost[(x, y)]:
                    cost[(x, y)] = new_cost
                    priority = new_cost + manhattan_distance((x, y), goal)
                    # Оценка для приоритета
                    heapq.heappush(priority_queue, (priority, (x, y)))
                    came_from[(x, y)] = current_point

    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Начальная и конечная точки
start = (0, 0)
goal = (4, 4)

result_path = astar(grid, start, goal)

# Вывод результата
print("Путь от A до B:")
for point in result_path:
    print(point)