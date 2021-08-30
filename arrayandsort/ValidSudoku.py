"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
"""
from typing import List


class ValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidItem(items: List[str]) -> bool:
            isValid = [False] * 9
            for i in range(9):
                if items[i] == ".":
                    continue
                val = ord(items[i]) - ord('0')
                isValid[val-1] = not isValid[val-1]
                if not isValid[val-1]:
                    return False

            return True

        for row in range(9):
            if not isValidItem(board[row]):
                return False
            cols = []
            for col in range(9):
                cols.append(board[col][row])
                #construct a little square
                if (row+1) % 3 == 0 and (col+1) % 3 == 0:
                    items = ["."] * 9
                    for r in range(row, row-3, -1):
                        for c in range(col, col-3, -1):
                            items[(row-r)*3+(col-c)] = board[c][r]
                    if not isValidItem(items):
                        return False
            if not isValidItem(cols):
                return False

        return True

board = [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]
vs = ValidSudoku()
isvalid = vs.isValidSudoku(board)

