"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""
from typing import List


class Searcha2DMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def searchRow() -> int:
            left, right = 0, m-1
            while left <= right:
                mid = (left+right) // 2
                if matrix[mid][0] <= target <= matrix[mid][n-1]:
                    return mid
                if matrix[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        def searchCol(row: int) -> bool:
            left, right = 0, n-1
            while left <= right:
                mid = (left+right) // 2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        row = searchRow()
        if row == -1:
            return False
        return searchCol(row)
