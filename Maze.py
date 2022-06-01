#http://bryukh.com/labyrinth-algorithms/#collapse-maze2graph-code

def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0       #kolone u nulti vrsti
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    #print(graph)
    for row, col in graph.keys():       #(i,j)/kljucevi od recnika 
        if row < height - 1 and not maze[row + 1][col]:  #znaci nije 0,sto znaci 1 i tu je zid i ne moze,u 0 i 11 row ne prolazi if  
            #print(maze[row+1][col])
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            #print(maze[row][col+1])
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph
           

from collections import deque


def find_path_bfs(maze):
    start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
    queue = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    while queue:
        path, current = queue.popleft()
        print(path,current)
        # path, current = queue.pop()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            #print(graph[current])
            queue.append((path + direction, neighbour))
            #print(direction)
            #print(path)
    return "NO WAY!"
#FIFO-red

def find_path_dfs(maze):
    start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
    stack = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    while stack:
        path, current = stack.pop()
        #print(path,current)
        if current == goal:
            return path     #ispada ne samo iz petlje nego i iz funkcije,nasli putanji i kraj
        if current in visited:
            continue
        visited.add(current)
        #print("-------")
        #print(current)
        #print(stack)
        for direction, neighbour in graph[current]:
            stack.append((path + direction, neighbour))
            
    return "NO WAY!"
#LIFO-stack

from heapq import heappop,heappush

def heuristic(cell,goal):
    return abs(cell[0]-goal[0])+abs(cell[1]-goal[1])

def find_path_astar(maze):
    start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
    pr_queue = []
    heappush(pr_queue, (0 + heuristic(start, goal), 0, "", start))
    visited = set()
    graph = maze2graph(maze)
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        #print(pr_queue)
        for direction, neighbour in graph[current]:
            heappush(pr_queue, (cost + heuristic(neighbour, goal), cost + 1,
                                path + direction, neighbour))
    return "NO WAY!"


MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

print(maze2graph(MAZE))
print(find_path_bfs(MAZE))
print(find_path_dfs(MAZE))
print(find_path_astar(MAZE))