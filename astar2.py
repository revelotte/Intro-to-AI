import heapq

# Locations and travel cost
places = {
    "Hotel": {"Museum": 3, "Restaurant": 2},
    "Museum": {"Beach": 4},
    "Restaurant": {"Beach": 2},
    "Beach": {}
}

# Heuristic values
heuristic = {
    "Hotel": 5,
    "Museum": 3,
    "Restaurant": 2,
    "Beach": 0
}

# A* Algorithm
def astar(start, goal):

    queue = [(0, start)]
    cost = {start: 0}
    parent = {start: None}

    while queue:
        _, current = heapq.heappop(queue)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, distance in places[current].items():
            new_cost = cost[current] + distance

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(queue, (priority, neighbor))
                parent[neighbor] = current


# Run Example
path = astar("Hotel", "Beach")

print("\nA* Example 2: Tourist Route")
print("---------------------------")
print("Start :", "Hotel")
print("Goal  :", "Beach")
print("Best Path :", " → ".join(path))