"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    Breadth-First Search (BFS) visits nodes level by level.

    A queue is used because BFS processes nodes in the exact
    order they are discovered (FIFO). This ensures we explore
    all neighbors of a node before moving deeper.

    Neighbors are added to the queue so they can be visited
    in the correct BFS order. This differs from DFS, which
    uses a stack and explores one path deeply before others.
    """

    # Handle missing start node safely
    if start not in graph:
        return []

    visited = set()          # Tracks nodes already visited
    queue = deque([start])   # Queue ensures level-by-level traversal
    order = []               # Stores BFS visit order

    visited.add(start)

    while queue:
        current = queue.popleft()  # Remove next node in BFS order
        order.append(current)

        # Visit each neighbor
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # Add neighbor to queue for later processing

    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # GRAPH STRUCTURE
    # ===============================
    #
    # Nodes represent campus buildings.
    # Edges represent walking paths between buildings.
    #
    graph = {
        "Library": ["Science Hall", "Cafeteria"],
        "Science Hall": ["Library", "Gym"],
        "Gym": ["Science Hall", "Dorms"],
        "Dorms": ["Gym"],
        "Cafeteria": ["Library", "Bookstore"],
        "Bookstore": ["Cafeteria"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    for node, neighbors in graph.items():
        print(f"{node} -> {neighbors}")

    # ===============================
    # BFS TRAVERSAL
    # ===============================
    print("\n=== BFS TRAVERSAL ===")

    start_node = "Library"
    print(f"Starting BFS from: {start_node}")

    order = bfs(graph, start_node)
    print("Traversal order:", order)

    # Add a new connection and show updated traversal
    graph["Library"].append("Dorms")
    print("\nAdded new edge: Library -> Dorms")

    updated_order = bfs(graph, start_node)
    print("Updated traversal order:", updated_order)

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # 1. Start from a different node
    print("Start from Gym:", bfs(graph, "Gym"))

    # 2. Missing start node
    print("Missing start node:", bfs(graph, "Unknown"))

    # 3. Disconnected graph
    disconnected_graph = {
        "A": ["B"],
        "B": ["A"],
        "X": []  # isolated node
    }
    print("Disconnected graph BFS from A:", bfs(disconnected_graph, "A"))
    print("Disconnected graph BFS from X:", bfs(disconnected_graph, "X"))

    # 4. Empty graph
    print("Empty graph BFS:", bfs({}, "Anything"))


if __name__ == "__main__":
    main()
