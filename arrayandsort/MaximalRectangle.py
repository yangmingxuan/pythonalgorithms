"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



Example 1:


Input: matrix =
    [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]

Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0


Constraints:

rows == matrix.length
cols == matrix[i].length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""
from typing import List


class MaximalRectangle:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        def largestRectangleArea(heights: List[int]) -> int:
            #saves the index of the first bar the left that is lower than current
            left_i = [0] * n
            left_i[0] = -1

            #saves the index of the first bar the right that is lower than current
            right_i = [0] * n
            right_i[n-1] = n

            for i in range(1, n):
                tmp = i -1
                while tmp >= 0 and heights[tmp] >= heights[i]:
                    tmp = left_i[tmp]
                left_i[i] = tmp

            for i in range(n-2, -1, -1):
                tmp = i + 1
                while tmp < n and heights[tmp] >= heights[i]:
                    tmp = right_i[tmp]
                right_i[i] = tmp

            res = 0
            for i in range(n):
                res = max(res, (right_i[i]-left_i[i]-1)*heights[i])

            return res

        heights = [0] * n
        max_area = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0

            max_area = max(max_area, largestRectangleArea(heights))

        return max_area

