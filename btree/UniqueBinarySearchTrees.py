"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.



Example 1:

Input: n = 3
Output: 5
    Explanation:
    Given n = 3, there are a total of 5 unique BST's:

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3


Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 19
"""

class UniqueBinarySearchTrees:
    def numTrees(self, n: int) -> int:
        #Catalan number f(n) = C(2n,n)/(n+1)
        sum = 1
        for i in range(2*n, n, -1):
            sum = sum*i//(2*n-i+1)

        return sum//(n+1)
