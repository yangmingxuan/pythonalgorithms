"""
Given the root of a binary tree, return the sum of values of its deepest leaves.


Example 1:
                 1
               /    \
              2      3
             / \      \
            4   5      6
           /            \
          7              8

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19


Constraints:

The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 100
"""
from typing import Optional
from collections import deque

from btree.TreeNode import TreeNode


class DeepestLeavesSum:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        while queue:
            size, dlsum = len(queue), 0  #there is a deeper layer than before
            while size > 0:
                node = queue.popleft()
                if not node.left and not node.right:
                    dlsum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1

        return dlsum

