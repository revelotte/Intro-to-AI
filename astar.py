import heapq

# Map of locations and distances
graph = {
    "Home": {"Mall": 2, "School": 5},
    "Mall": {"Park": 4, "School": 2},
    "School": {"Park": 1},
    "Park": {}
}

# Estimated distance to the goal (heuristic)
heuristic = {
    "Home": 7,
    "Mall": 4,
    "School": 2,
    "Park": 0
}

# A* Algorithm
def astar(start, goal):

    open_list = [(0, start)]
    cost = {start: 0}
    parent = {start: None}

    while open_list:
        _, node = heapq.heappop(open_list)

        # If goal is reached, build the path
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor, distance in graph[node].items():
            new_cost = cost[node] + distance

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                parent[neighbor] = node


# Run Example
path = astar("Home", "Park")

print("A* Example 1: Going to the Park")
print("-------------------------------")
print("Start :", "Home")
print("Goal  :", "Park")
print("Best Path :", " → ".join(path))