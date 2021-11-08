"""
Given the root of a binary tree, return the sum of all left leaves.



Example 1:
                3
               / \
              9   20
                 / \
                15  7


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""
from typing import Optional

from btree.TreeNode import TreeNode


class SumofLeftLeaves:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = []
        q.append(root)
        while q:
            size = len(q)
            while size > 0:
                node = q.pop()
                if node.left and not node.left.left and not node.left.right:
                    ans += node.left.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1

        return ans
