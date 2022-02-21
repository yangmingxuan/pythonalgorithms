"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:
        3
       / \
      9  20
        /  \
       15   7


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
import collections
from typing import Optional

from btree.TreeNode import TreeNode


class MaximumDepthofBinaryTree:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        treequeue = collections.deque()
        treequeue.append(root)

        while treequeue:
            size = len(treequeue)
            for i in range(size):
                node = treequeue.popleft()
                if node.left:
                    treequeue.append(node.left)
                if node.right:
                    treequeue.append(node.right)

            depth += 1

        return depth
