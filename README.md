# cs6212-project3


# 20231026 Proj 3

## Project 3

Shi Qiu, HaiDong Zheng, YiCheng Chu, Yiming Xu G26512274


**Date: October 26, 2023**

### 1 Problem Analysis
#### 1.1 Problem Statement
Given a maze, find the target using Depth-First Searching(DFS) in linear time.
#### 1.2 Problem Solution
**Assumptions**:


A maze is stored as a 2-D array in which 0 represents obstacle and 1 represents empty space.


**Intuition**:
Use an array to record if the current cell has been visted. The maze array is overwritten in the code to record this information.
Each time a new cell is visited, update the array. Then recursively find if there is a path from the adjacent cells of the current cell to the target. an adjacent cell means the cell is not an abstacle, a visted cell or out of boundary. When failing to find a path from all the adjacent cells of the current cell, backtrack to the last cell and set the current cell unvisited to allow other pathes to use this cell.

### 2 Pseudocode
<pre>
Function is_valid(x, y, maze):
    IF x is between 0 and the number of rows in maze AND 
       y is between 0 and the number of columns in maze AND 
       maze[x][y] equals 1:
        Return TRUE
    ELSE:
        Return FALSE

Function maze_dfs_recursion(maze, x, y, target, path):
    IF x and y coordinates match target coordinates:
        Add (x, y) to path
        Return TRUE
    
    IF is_valid(x, y, maze) is FALSE:
        Return FALSE

    // Mark the current cell as visited
    Set maze[x][y] to -1

    // Define possible directions: Right, Down, Left, Up
    Directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    FOR each direction in Directions:
        IF maze_dfs_recursion using next cell in the direction is TRUE:
            Add (x, y) to path
            Return TRUE

    // If no path found, backtrack to the previous position
    Set maze[x][y] to 1
    
    Return FALSE
</pre>

### 3 Theoretical Analysis of Time Complexity

The core computational challenge of the DFS algorithm for maze solving is the traversal of all possible paths until the exit is found. The time complexity of this algorithm is $O(n)$ where n is the number of cells in the maze. While the algorithm involves other steps, such as identifying the start point, the complexities of these steps are insignificant compared to the traversal.

### 4 Numerical Results

#### 4.1 Program Listing

this is the DFS implementation for Maze


![(300)image.png|300](https://raw.githubusercontent.com/ryan0980/expert-potato/main/img/202310262221662.png)


The dataset sizes for which the algorithm is tested were determined as follows: start from 5\*5, add 5 at each side at a time, repate 80 times till 405\*405

#### 4.2 Data Normalization Notes

The data was normalized using a logarithmic scale (plt scale log).

#### 4.3 Output Numerical Data

| Maze Size (NxN) | Experimental Time  | Theoretical|
|-----------------|------------------------|-----------------------|
| 5x5 | -10.780557571256935 | -10.953309677034806 |
| 10x10 |-9.99999845291695 | -9.567015315914915 |
| 15x15 | -9.010670176847615 | -8.756085099698586 |
| 20x20 | -8.39941015575984 | -8.180720954795024|
| … | … | … |
| 400x400 |-2.214789440295657 | -2.214413972100763|
| 405x405 |-2.7684277909334902 |-2.1892564076870427 |

### 5 Graph

![image.png](https://raw.githubusercontent.com/ryan0980/expert-potato/main/img/202310262217260.png)

#### 5.1 Graph Observations

The graph shows a close alignment between experimental and theoretical assessments of the DFS algorithm in maze-solving, especially as maze size increases. However, discrepancies are observed, likely influenced by the random maze generation process. Conducting the task multiple times and using the average results could potentially mitigating the effects of random variations and external factors.

### 6 Conclusions

Our experimental findings closely align with the theoretical assessment, reiterating the $O(n)$ time complexity of the DFS algorithm for maze-solving problems. This research confirms the efficiency and effectiveness of DFS in tackling such computational challenges.

//ref: <https://medium.com/swlh/solving-mazes-with-depth-first-search-e315771317ae>
