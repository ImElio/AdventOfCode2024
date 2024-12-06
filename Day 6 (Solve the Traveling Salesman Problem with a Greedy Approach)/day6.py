def tsp_greedy(graph, start=0):
    n = len(graph)
    visited = [False] * n
    path = [start]
    total_cost = 0
    current = start
    visited[current] = True

    for _ in range(n - 1):
        next_node = None
        min_cost = float('inf')
        for neighbor in range(n):
            if not visited[neighbor] and graph[current][neighbor] < min_cost:
                min_cost = graph[current][neighbor]
                next_node = neighbor
        if next_node is not None:
            visited[next_node] = True
            path.append(next_node)
            total_cost += min_cost
            current = next_node

    total_cost += graph[current][start]
    path.append(start)
    return path, total_cost

if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    start_node = 0
    path, cost = tsp_greedy(graph, start_node)
    print("Percorso:", path)
    print("Costo totale:", cost)
