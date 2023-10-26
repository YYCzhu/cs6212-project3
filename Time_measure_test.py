def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

def dfs(x, y, maze, end, path):
    if (x, y) == end:
        path.append((x, y))
        return True
    if not is_valid(x, y, maze):
        return False

    # Mark the current cell as visited
    maze[x][y] = -1

    # Explore in four possible directions: Up, Down, Left, Right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        if dfs(x + dx, y + dy, maze, end, path):
            path.append((x, y))
            return True

    # If no path found, backtrack
    maze[x][y] = 1  # Reset the cell's value to open

    return False

def dfs_maze(maze, start, end):
    path = []

    if dfs(start[0], start[1], maze, end, path):
        path.reverse()  # Reverse the path to get it from start to end
        return path
    else:
        return []


import time


def measure_time(func, *args, **kwargs):
    """
    Measures the execution time of the given function.

    Parameters:
    - func: the function to execute
    - *args, **kwargs: arguments to pass to the function

    Returns:
    - result of the function
    - time taken to execute the function in seconds
    """

    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    duration = end_time - start_time

    return result, duration


import random


def Maze_init(n):
    # Step 1: Create a grid full of walls
    maze = [[0 for _ in range(n)] for _ in range(n)]

    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Define a function to get the neighboring walls of a cell
    def get_neigh_walls(cell):
        x, y = cell
        walls = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 0:
                walls.append((nx, ny))
        return walls

    # Step 2: Pick a cell and mark it as a path
    start_cell = (0, 0)
    maze[start_cell[0]][start_cell[1]] = 1
    wall_list = get_neigh_walls(start_cell)

    # Step 3: While there are walls in the wall list
    while wall_list:
        wall = random.choice(wall_list)
        wall_list.remove(wall)

        x, y = wall
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                neighbors.append((nx, ny))

        count_visited = sum([maze[nx][ny] for nx, ny in neighbors])

        if count_visited == 1:
            maze[x][y] = 1
            wall_list.extend(get_neigh_walls((x, y)))

    maze[n - 1][n - 1] = 1
    return maze


def complexity_calculator(n):
    maze=Maze_init(n)
    entrance = (0, 0)
    exit = (n-1,n-1)
    # for fow in maze:
    #     print(fow)

    path, exec_time = measure_time(dfs_maze, maze,entrance, exit)
    return exec_time

    # print(f"Result: {path}")
    # print(f"Execution time: {exec_time} seconds")
    # if path:
    #     print("Path found from entrance to exit:")
    #     for step in path:
    #         print(step)
    # else:
    #     print("No path from entrance to exit.")

file_path = "time_recorder_PJ3.txt"

time_recorder=[]
scale=[]
for i in range(80):
    print(i,"'s iter is done")
    time_recorder.append(complexity_calculator(5+i*5))
    scale.append(5+i*5)

with open("record.txt", "w") as file:
    for item in time_recorder:
        file.write(f"{item}\n")  # Writing each item on a new line


