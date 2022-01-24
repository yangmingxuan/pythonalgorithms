"""
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.



Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""
from typing import List


class CheckifThereisaValidPathinaGrid:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True

        def nextDirection(cell: int, prevR: int, prevC: int):
            if cell == 1 and prevR == 0:
                if prevC == -1:
                    return (0, 1)
                elif prevC == 1:
                    return (0, -1)
            elif cell == 2 and prevC == 0:
                if prevR == -1:
                    return (1, 0)
                elif prevR == 1:
                    return (-1, 0)
            elif cell == 3:
                if prevR == 0 and prevC == -1:
                    return (1, 0)
                elif prevR == 1 and prevC == 0:
                    return (0, -1)
            elif cell == 4:
                if prevR == 1 and prevC == 0:
                    return (0, 1)
                elif prevR == 0 and prevC == 1:
                    return (1, 0)
            elif cell == 5:
                if prevR == 0 and prevC == -1:
                    return (-1, 0)
                elif prevR == -1 and prevC == 0:
                    return (0, -1)
            elif cell == 6:
                if prevR == -1 and prevC == 0:
                    return (0, 1)
                elif prevR == 0 and prevC == 1:
                    return (-1, 0)

            return (0, 0)

        def isValidNextCell(nextR: int, nextC: int, nextcell: int) -> bool:
            if nextR == 0 and nextC == 1 and nextcell in (1, 3, 5):
                return True
            elif nextR == 0 and nextC == -1 and nextcell in (1, 4, 6):
                return True
            elif nextR == 1 and nextC == 0 and nextcell in (2, 5, 6):
                return True
            elif nextR == -1 and nextC == 0 and nextcell in (2, 3, 4):
                return True

            return False


        def checkPath(cell: int, prevR: int, prevC: int) -> bool:
            visited = [[False] * n for _ in range(m)]
            visited[0][0] = True
            r, c = 0, 0
            while True:
                nextR, nextC = nextDirection(cell, prevR, prevC);
                if nextR == 0 and nextC == 0:
                    return False
                r += nextR
                c += nextC
                prevR = -nextR
                prevC = -nextC
                if r < 0 or r >= m or c < 0 or c >= n or visited[r][c]:
                    return False
                nextcell = grid[r][c]
                if not isValidNextCell(nextR, nextC, nextcell):
                    return False

                if r == m - 1 and c == n - 1:
                    return True

                visited[r][c] == True
                cell = nextcell

        cell = grid[0][0]
        if cell in (1, 3, 5):
            return checkPath(cell, 0, -1)
        elif cell in (2, 6):
            return checkPath(cell, -1, 0)
        elif cell == 4:
            return checkPath(cell, 1, 0) or checkPath(cell, 0, 1)


