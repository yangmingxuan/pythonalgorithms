"""
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)



Example 1:
               8
             /   \
            3     10
           / \     \
          1   6     14
             / \    /
            4   7  13
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.


Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""
from btree import TreeNode


class MaximumDifferenceBetweenNodeandAncestor:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode, curMax: int, curMin: int) -> int:
            if not node: #the end, return this path's maximum - minimum
                return curMax - curMin
            curMax = max(curMax, node.val)
            curMin = min(curMin, node.val)
            maxLeftDifference = dfs(node.left, curMax, curMin)
            maxRightDifference = dfs(node.right, curMax, curMin)
            return max(maxLeftDifference, maxRightDifference)

        return dfs(root, root.val, root.val)
