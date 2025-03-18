from collections import deque

# Graph representation (Adjacency List)
def bfs_shortest_path(city_map, start, goal):
    if start == goal:
        return [start]
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]  
        if node not in visited:
            neighbors = city_map.get(node, [])
            
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            
                    if neighbor == goal:
                    return new_path
        visited.add(node)
    return None

city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

start = 'Home'
goal = 'Hospital'
shortest_path = bfs_shortest_path(city_map, start, goal)
#Running the searches
print("Rute terpendek dari", start, "ke", goal, ":", shortest_path)