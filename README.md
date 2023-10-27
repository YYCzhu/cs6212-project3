# cs6212-project3


# 20231026 Proj 3

## Project 3

Shi Qiu, HaiDong Zheng, YiCheng Chu
**Date: October 26, 2023**

### 1 Problem Statement

Our task is to analyze the maze-solving problem using the Depth-First Search (DFS) algorithm.
1. **Start Point**: Begin at the maze entrance.
2. **Explore Path**: Traverse open paths, avoiding walls.
3. **Mark Traversed**: Record cells as visited to prevent revisiting.
4. **Check Neighbors**: Evaluate adjacent cells for valid moves.
5. **Backtrack**: When a dead end is reached, backtrack to a cell with unexplored paths.
6. **Identify Exit**: Continue until the maze exit is reached or all paths are explored.
7. **End Search**: Return the successful path or indicate no solution if the exit isn't found.

### 2 Theoretical Analysis

The core computational challenge of the DFS algorithm for maze solving is the traversal of all possible paths until the exit is found. The time complexity of this algorithm is $O(n)$ where n is the number of cells in the maze. While the algorithm involves other steps, such as identifying the start point, the complexities of these steps are insignificant compared to the traversal.

### 3 Experimental Analysis

#### 3.1 Program Listing

this is the DFS implementation for Maze
![(300)image.png|300](https://raw.githubusercontent.com/ryan0980/expert-potato/main/img/202310262221662.png)
The dataset sizes for which the algorithm is tested were determined as follows: start from 5\*5, add 5 at each side at a time, repate 80 times till 405\*405

#### 3.2 Data Normalization Notes

The data was normalized using a logarithmic scale (plt scale log).

#### 3.3 Output Numerical Data

| Maze Size (NxN) | Experimental Time  | Theoretical|
|-----------------|------------------------|-----------------------|
| 5x5 | -10.780557571256935 | -10.953309677034806 |
| 10x10 |-9.99999845291695 | -9.567015315914915 |
| 15x15 | -9.010670176847615 | -8.756085099698586 |
| 20x20 | -8.39941015575984 | -8.180720954795024|
| … | … | … |
| 400x400 |-2.214789440295657 | -2.214413972100763|
| 405x405 |-2.7684277909334902 |-2.1892564076870427 |

#### 3.4 Graph

![image.png](https://raw.githubusercontent.com/ryan0980/expert-potato/main/img/202310262217260.png)

#### 3.5 Graph Observations

The graph shows a close alignment between experimental and theoretical assessments of the DFS algorithm in maze-solving, especially as maze size increases. However, discrepancies are observed, likely influenced by the random maze generation process. Conducting the task multiple times and using the average results could potentially mitigating the effects of random variations and external factors.

### 4 Conclusions

Our experimental findings closely align with the theoretical assessment, reiterating the $O(n)$ time complexity of the DFS algorithm for maze-solving problems. This research confirms the efficiency and effectiveness of DFS in tackling such computational challenges.

//ref: <https://medium.com/swlh/solving-mazes-with-depth-first-search-e315771317ae>
