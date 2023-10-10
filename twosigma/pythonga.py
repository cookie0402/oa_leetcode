# from_nodes = [0,1,2,3,4,5,6,7]
# to_nodes = [1,2,3,4,5,6,7,8]
#
#
# from_nodes = [0,0,1,1,3,3,5,7,8]
# to_nodes = [4,1,2,3,5,7,6,8,9]
# x = 4
# y = 6
# z = 9
import collections
from collections import deque
from collections import defaultdict


def bfs_shortest_path(graph, start, target):
    visited = set()
    queue = deque([(start, 0)])  # Node and distance

    while queue:
        node, distance = queue.popleft()

        if node == target:
            return distance

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

    return float('inf')  # If no path exists

from_nodes = [0,1,2,3,4,5,6,7]
to_nodes = [1,2,3,4,5,6,7,8]

graph = defaultdict(list)
for u, v in zip(from_nodes, to_nodes):
    graph[u].append(v)
    graph[v].append(u)
print(graph)

nodes = set(from_nodes + to_nodes)
x, y, z = 3, 4, 5
count = 0


for node in nodes:
    if node ==x or node ==y or node ==z:
        continue

    px = bfs_shortest_path(graph, node, x)
    py = bfs_shortest_path(graph, node, y)
    pz = bfs_shortest_path(graph, node, z)



    path_lengths = [px, py, pz]
    path_lengths.sort()

    if path_lengths[0]**2 + path_lengths[1]**2 == path_lengths[2]**2:
        print("node: ", node, "->x(3):", px, "->y(4):", py, "->z(5):", pz)
        count += 1

print(count)
