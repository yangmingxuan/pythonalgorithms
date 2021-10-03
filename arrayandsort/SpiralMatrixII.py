"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
"""
from typing import List


class SpiralMatrixII:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        count = 1
        rowtop, rowbottom = 0, n-1
        colleft, colright = 0, n-1
        while rowtop <= rowbottom and colleft <= colright:
            for col in range(colleft, colright+1):
                matrix[rowtop][col] = count
                count += 1
            for row in range(rowtop+1, rowbottom+1):
                matrix[row][colright] = count
                count += 1
            if rowtop < rowbottom and colleft < colright:
                for col in range(colright-1, colleft-1, -1):
                    matrix[rowbottom][col] = count
                    count += 1
                for row in range(rowbottom-1, rowtop, -1):
                    matrix[row][colleft] = count
                    count += 1
            rowtop += 1
            rowbottom -= 1
            colleft += 1
            colright -= 1

        return matrix
