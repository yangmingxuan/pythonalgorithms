"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:

    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""
import itertools
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l, m, n = len(word), len(board), len(board[0])
        def backtrace(row: int, col: int, idx: int) -> bool:
            dxy = [(0,1), (0,-1), (1,0), (-1,0)]

            #If the entire string is compared
            if idx == l:
                return True

            #If moved out of bounds, or characters are not equal
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[idx]:
                return False

            board[row][col] = '*' #Visited
            ret = False
            for r, c in dxy:
                if backtrace(row+r, col+c, idx+1):
                    ret = True
                    break

            board[row][col] = word[idx]
            return ret

        for r, c in itertools.product(range(m), range(n)):
            if backtrace(r, c, 0):
                return True

        return False

