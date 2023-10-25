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

# Example usage:
maze = [
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1]
]

entrance = (0, 0)
exit = (4, 4)

path = dfs_maze(maze, entrance, exit)

if path:
    print("Path found from entrance to exit:")
    for step in path:
        print(step)
else:
    print("No path from entrance to exit.")
