"""
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.



Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5


Constraints:

n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
"""
from typing import List


class KthSmallestElementinaSortedMatrix:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def countless(mid: int) -> int:
            col = n -1
            count = 0
            for row in range(n):
                while col >= 0 and matrix[row][col] > mid:
                    col -= 1
                count += col+1

            return count

        low, high = matrix[0][0], matrix[n-1][n-1]
        while low <= high:
            mid = (low + high) // 2
            if countless(mid) < k:
                low = mid + 1
            else:
                high = mid - 1

        return low
