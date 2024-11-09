import heapq  # Импортируем модуль heapq для работы с приоритетной очередью (куча)
import networkx as nx  # Импортируем модуль networkx для работы с графами


def get_path(predecessors, end, distances):
    path = []
    if distances[end] == 10e9:
        return None  # Если расстояние равно "бесконечности", пути нет
    while end != -1:
        path.append(end)
        end = predecessors[end]
    path.reverse()  # Путь восстанавливается в обратном порядке, поэтому нужно развернуть его
    return path


def dijkstra(edges, num_nodes, start):
    # Инициализируем пустой граф в виде списка смежности.
    graph = [[] for _ in range(num_nodes)]

    # Заполняем граф на основе списка рёбер (edges).
    for u, v, w in edges:
        graph[u].append((v, w))  # Для каждой вершины u добавляем в список её соседей вершину v и вес w.

    # Инициализируем список минимальных расстояний от начальной вершины до каждой другой.
    distances = [10e9] * num_nodes
    distances[start] = 0  # Расстояние от стартовой вершины до самой себя всегда 0.

    # Инициализируем список предшественников для восстановления путей.
    predecessors = [-1] * num_nodes  # Для каждой вершины хранится индекс её предшественника в пути.

    # Инициализируем приоритетную очередь (кучу) и добавляем туда стартовую вершину с расстоянием 0.
    priority_queue = [(0, start)]

    # Запускаем цикл, пока есть элементы в очереди (пока не обработаем все вершины).
    while priority_queue:
        # Достаём вершину с минимальным расстоянием из приоритетной очереди.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Если текущее расстояние больше, чем записанное в distances для этой вершины,
        # значит, мы уже нашли более короткий путь ранее, поэтому продолжаем дальше.
        if current_distance > distances[current_node]:
            continue

        # Обрабатываем всех соседей текущей вершины.
        for neighbor, weight in graph[current_node]:
            # Вычисляем новое возможное расстояние до соседа через текущую вершину.
            distance = current_distance + weight

            # Если это расстояние меньше того, что уже записано для соседа, обновляем его.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node  # Запоминаем текущую вершину как предшественника для соседа.
                # Добавляем соседа в приоритетную очередь для дальнейшей обработки.
                heapq.heappush(priority_queue, (distance, neighbor))

    # Восстанавливаем пути до каждой вершины
    paths = [get_path(predecessors, i, distances) for i in range(num_nodes)]
    return distances, paths


edges = [
    (0, 1, 1),
    (0, 3, 3),
    (1, 3, 1),
    (1, 2, 3),
    (1, 4, 2),
    (3, 2, 3),
    (3, 4, 1),
    (4, 2, 2)
]
routes = [
    (0, 4),
    (4, 1),
    (0, 2)
]


# Функция для нахождения кратчайшего пути
def find_shortest_paths(edges, routes):
    graph = nx.Graph()
    for u, v, w in edges:
        graph.add_edge(u, v, weight=w)
    shortest_paths = {}
    for start, end in routes:
        path = nx.dijkstra_path(graph, start, end)
        distance = nx.dijkstra_path_length(graph, start, end)
        shortest_paths[(start, end)] = (path, distance)
    return shortest_paths


# Получаем кратчайшие пути
result = find_shortest_paths(edges, routes)

# Выводим результаты
for (start, end), (path, distance) in result.items():
    print(f"Кратчайший путь от {start} до {end}: {path} с расстоянием {distance}")

num_nodes = 5  # Количество вершин в графе
start_node = 0  # Стартовая вершина

# Получаем минимальные расстояния и пути до каждой вершины
distances, paths = dijkstra(edges, num_nodes, start_node)

# Выводим минимальные расстояния и пути
for i in range(num_nodes):
    print(f"Минимальное расстояние до вершины {i}: {distances[i]}")
    print(f"Путь до вершины {i}: {paths[i]}")
