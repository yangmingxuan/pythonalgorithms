"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
from typing import List


class LongestIncreasingPathinaMatrix:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        posLongestPath = [[0] * n for _ in range(m)]

        def longestPath(row: int, col: int) -> int:
            if posLongestPath[row][col] > 0:
                return posLongestPath[row][col]
            maxpath = 0
            directions = ((0,1),(0,-1),(1,0),(-1,0))
            for x, y in directions:
                newrow = row + x
                newcol = col + y
                if 0 <= newrow < m and 0 <= newcol < n and matrix[newrow][newcol] > matrix[row][col]:
                    maxpath = max(maxpath, longestPath(newrow, newcol))

            maxpath += 1  #include this position
            posLongestPath[row][col] = maxpath
            return maxpath

        return max(longestPath(i, j) for i in range(m) for j in range(n))
