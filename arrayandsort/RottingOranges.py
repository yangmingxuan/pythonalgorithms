"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from typing import List


class RottingOranges:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        freshcount = 0
        rotton = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshcount += 1
                elif grid[i][j] == 2:
                    rotton.append((i,j))

        if freshcount == 0:
            return 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        step = 0
        while rotton:
            size = len(rotton)
            for k in range(size):
                cell = rotton.pop(0)
                for r,c in directions:
                    nrow, ncol = cell[0]+r, cell[1]+c
                    if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n:
                        if grid[nrow][ncol] == 1:
                            grid[nrow][ncol] = 2
                            freshcount -= 1
                            rotton.append((nrow,ncol))

            step += 1

        return step-1 if freshcount == 0 else -1


