"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
from typing import List


class SurroundedRegions:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])

        #If it is an O on the boundary, or an O connected to the boundary O in four dimensions, set the flag
        def DFS(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = '#'
            DFS(r, c+1)
            DFS(r, c-1)
            DFS(r+1, c)
            DFS(r-1, c)

            return

        for c in range(n):
            if board[0][c] == 'O':
                DFS(0, c)
            if board[-1][c] == 'O':
                DFS(m-1, c)
        for r in range(m):
            if board[r][0] == 'O':
                DFS(r, 0)
            if board[r][-1] == 'O':
                DFS(r, n-1)

        #If it is an O on the boundary, or an O connected to the boundary O in four dimensions, do not change, other transfer into X
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == '#':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'

        return
