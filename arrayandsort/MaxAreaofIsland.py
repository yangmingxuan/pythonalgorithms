"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
from typing import List


class MaxAreaofIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return 0
        visited = [[False] * n for _ in range(m)]

        def area(row: int, col: int) -> int:
            if row < 0 or row >= m or col < 0 or col >= n or visited[row][col] or grid[row][col] == 0:
                return 0
            visited[row][col] = True
            return 1 + area(row-1, col) + area(row+1, col) + area(row, col-1) + area(row, col+1)

        maxarea = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    maxarea = max(maxarea, area(i, j))

        return maxarea
