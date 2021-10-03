"""
 * Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

    Example 1:

    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]
    Example 2:

    Input:
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
from typing import List


class SpiralMatrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lret = []
        if not matrix: return lret
        rowtop , rowbottom = 0, len(matrix)-1
        colleft, colright = 0, len(matrix[0])-1
        while rowtop <= rowbottom and colleft <= colright:
            for col in range(colleft,colright+1):
                lret.append(matrix[rowtop][col])
            for row in range(rowtop+1, rowbottom+1):
                lret.append(matrix[row][colright])
            if colleft < colright and rowtop < rowbottom:
                for col in range(colright-1,colleft-1,-1):
                    lret.append(matrix[rowbottom][col])
                for row in range(rowbottom-1,rowtop,-1):
                    lret.append(matrix[row][colleft])
            rowtop += 1
            rowbottom -= 1
            colleft += 1
            colright -= 1

        return lret
