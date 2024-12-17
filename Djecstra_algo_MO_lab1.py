# аддитивный критерий
def algodijkstra_add(matrix, start):
    n = len(matrix)
    dist = [float('inf')] * n  
    dist[start] = 0 
    visited = [False] * n  

    for _ in range(n):
        min_dist = float('inf')
        min_dot = -1
        for i in range(n):
            if (visited[i] == False) and (dist[i] < min_dist):
                min_dist = dist[i]
                min_dot = i

        if min_dot == -1:  
            break

        visited[min_dot] = True

        for i in range(n):
            if matrix[min_dot][i] != 0 and not visited[i]:
                new_dist = dist[min_dot] + matrix[min_dot][i]
                if new_dist < dist[i]:
                    dist[i] = new_dist

    return dist[n-1]

# критерий типа максимум 
def algodijkstra_min_max_edge(matrix, start):
    n = len(matrix)
    max_edge = [float('inf')] * n  
    max_edge[start] = 0  
    visited = [False] * n  

    for _ in range(n):
        min_val = float('inf')
        min_dot = -1
        for i in range(n):
            if (visited[i] == False) and (max_edge[i] < min_val):
                min_val = max_edge[i]
                min_dot = i

        if min_dot == -1:
            break

        visited[min_dot] = True

        for i in range(n):
            if matrix[min_dot][i] != 0 and not visited[i]:
                new_max_edge = max(max_edge[min_dot], matrix[min_dot][i])
                if new_max_edge < max_edge[i]:
                    max_edge[i] = new_max_edge

    return max_edge[n-1]


# задаем матрицу смежности 
matrix = [
    [0, 5, 8, 3, 0],
    [0, 0, 2, 0, 6],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0]
]

start = 0
distance = algodijkstra_add(matrix, start)

print(f"Значение аддитивного критерия = {distance}")

start = 0
result = algodijkstra_min_max_edge(matrix, start)

print(f"Значение критерия типа максимум = {result}")
