import heapq

def un_cs(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start, [start]))
    explored = set()

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        if node == goal:
            print("Optimal path :", path)
            print("Path cost :", cost)
            return

        if node in explored:
            continue

        explored.add(node)

        for neighbour, edge_cost in graph[node]:
            if neighbour not in explored:
                heapq.heappush(frontier,
                               (cost + edge_cost, neighbour, path + [neighbour]))

    print("No path found")


# Input section
graph = {}
n = int(input("Enter no.of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    graph[node] = []

edges = int(input("Enter no.of edges from node: "))

for _ in range(edges):
    neighbour = input("Enter neighbour: ")
    cost = int(input("Enter edge cost: "))
    graph[node].append((neighbour, cost))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# Run UCS
un_cs(graph, start, goal)