import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position  # (x, y)

        self.g = 0
        self.h = 0 
        self.f = 0 

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f 
def astar(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # Genera i figli (vicini)
        (x, y) = current_node.position
        neighbors = [
            (x - 1, y),     # Sinistra
            (x + 1, y),     # Destra
            (x, y - 1),     # Sopra
            (x, y + 1),     # Sotto
            # movimenti diagonali:
            # (x - 1, y - 1),
            # (x - 1, y + 1),
            # (x + 1, y - 1),
            # (x + 1, y + 1),
        ]

        for next_position in neighbors:
            if (0 <= next_position[0] < len(maze[0])) and (0 <= next_position[1] < len(maze)):
                if maze[next_position[1]][next_position[0]] == 0:
                    neighbor = Node(current_node, next_position)
                    if neighbor.position in closed_list:
                        continue

                    # valori = g, h, f
                    neighbor.g = current_node.g + 1
                    neighbor.h = abs(neighbor.position[0] - end_node.position[0]) + abs(neighbor.position[1] - end_node.position[1])
                    neighbor.f = neighbor.g + neighbor.h

                    if any(open_node for open_node in open_list if neighbor == open_node and neighbor.g >= open_node.g):
                        continue

                    heapq.heappush(open_list, neighbor)

    return None 

if __name__ == "__main__":
    # (0 = libero, 1 = ostacolo)
    maze = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
    ]

    start = (0, 0)  # (x, y)
    end = (5, 4)

    path = astar(maze, start, end)
    if path:
        print("Percorso trovato:")
        print(path)
    else:
        print("Nessun percorso trovato.")
