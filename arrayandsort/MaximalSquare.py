"""
iven an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.



Example 1:

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
from typing import List


class MaximalSquare:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols+1) for _ in range(rows+1)]

        squarelen = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    dp[row+1][col+1] = 1 + min(dp[row][col+1],dp[row+1][col],dp[row][col])
                    squarelen = max(squarelen, dp[row+1][col+1])

        return squarelen*squarelen
