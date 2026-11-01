import math
from collections import deque


# Build the graph using an adjacency list.
def create_graph():
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"C": 10, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3}
    }
    return graph


# Print the adjacency list of the graph.
def show_adjacency_list(graph):
    print("Adjacency List:")
    for vertex in sorted(graph):
        edges = []
        for neighbour in sorted(graph[vertex]):
            edges.append(f"{neighbour}({graph[vertex][neighbour]})")
        print(vertex, ":", ", ".join(edges))


# Create and print the weighted adjacency matrix.
def show_matrix(graph):
    vertices = sorted(graph)
    print("\nWeighted Adjacency Matrix:")
    print("   ", " ".join(vertices))

    for vertex in vertices:
        row = []
        for neighbour in vertices:
            if vertex == neighbour:
                row.append("0")
            elif neighbour in graph[vertex]:
                row.append(str(graph[vertex][neighbour]))
            else:
                row.append("inf")
        print(vertex, "  ", " ".join(f"{value:>2}" for value in row))


# Visit vertices level by level using breadth-first search.
def bfs(graph, start):
    visited = []
    queue = deque([start])
    seen = {start}

    while queue:
        vertex = queue.popleft()
        visited.append(vertex)

        for neighbour in sorted(graph[vertex]):
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)

    return visited


# Visit vertices by going as deep as possible using depth-first search.
def dfs(graph, start):
    visited = []
    seen = set()

    def visit(vertex):
        seen.add(vertex)
        visited.append(vertex)

        for neighbour in sorted(graph[vertex]):
            if neighbour not in seen:
                visit(neighbour)

    visit(start)
    return visited


# Find shortest distances from the start vertex using Dijkstra's algorithm.
def dijkstra(graph, start):
    distance = {vertex: math.inf for vertex in graph}
    previous = {vertex: None for vertex in graph}
    finalized = set()
    order = []

    distance[start] = 0

    while len(finalized) < len(graph):
        remaining = [v for v in graph if v not in finalized]
        current = min(remaining, key=lambda v: (distance[v], v))

        if distance[current] == math.inf:
            break

        finalized.add(current)
        order.append(current)

        for neighbour in sorted(graph[current]):
            if neighbour not in finalized:
                new_distance = distance[current] + graph[current][neighbour]
                if new_distance < distance[neighbour]:
                    distance[neighbour] = new_distance
                    previous[neighbour] = current

    return distance, previous, order


# Rebuild the shortest path by following predecessor values.
def get_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        if current == start:
            break
        current = previous[current]

    path.reverse()
    if not path or path[0] != start:
        return []
    return path


# Run all graph operations.
if __name__ == "__main__":
    graph = create_graph()

    print("Graph representation")
    show_adjacency_list(graph)
    show_matrix(graph)

    print("\nTraversals starting from A")
    print("BFS:", " -> ".join(bfs(graph, "A")))
    print("DFS:", " -> ".join(dfs(graph, "A")))

    print("\nDijkstra's algorithm from A")
    distance, previous, order = dijkstra(graph, "A")

    print("Finalized vertex | Distance | Predecessor")
    for vertex in order:
        pred = previous[vertex] if previous[vertex] is not None else "-"
        print(f"{vertex:^16} | {distance[vertex]:^8} | {pred}")

    path = get_path(previous, "A", "F")
    print("Shortest path to F:", " -> ".join(path))
    print("Total cost:", distance["F"])

