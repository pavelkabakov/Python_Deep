'''
Задача №5. Дейкстра
Дан ориентированный взвешенный граф. Найдите кратчайшее расстояние от одной заданной вершины до другой.

Входные данные
В первой строке содержатся три числа: N, S и F (1≤ N≤ 100, 1≤ S, F≤ N), где N – количество вершин графа,
 S – начальная вершина, а F – конечная. В следующих N строках вводится по N чисел, не превосходящих 100,
  – матрица смежности графа, где -1 означает отсутствие ребра между вершинами, а любое неотрицательное число
  – присутствие ребра данного веса. На главной диагонали матрицы записаны нули.

Выходные данные
Требуется вывести искомое расстояние или -1, если пути между указанными вершинами не существует.

Примеры
входные данные
3 2 1
0 1 1
4 0 1
2 1 0
выходные данные
3
'''

import heapq


def dijkstra(graph, N, S, F):
    # Массив расстояний и посещенных вершин
    dist = [float('inf')] * N
    dist[S] = 0
    visited = [False] * N

    # Очередь с приоритетом (min-heap)
    pq = [(0, S)]  # (расстояние, вершина)

    while pq:
        d, u = heapq.heappop(pq)

        # Если вершина уже посещена, пропускаем
        if visited[u]:
            continue

        visited[u] = True

        # Обновляем расстояния до соседей
        for v in range(N):
            weight = graph[u][v]
            if weight != -1 and not visited[v]:
                new_dist = d + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

    # Возвращаем расстояние до конечной вершины или -1, если недостижима
    return dist[F] if dist[F] != float('inf') else -1


# Ввод данных
N, S, F = map(int, input().split())
S -= 1  # Приводим индексацию к нулям
F -= 1

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# Вызываем алгоритм Дейкстры
result = dijkstra(graph, N, S, F)
print(result)