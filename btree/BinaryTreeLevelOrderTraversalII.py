"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
from typing import List

from btree import TreeNode


class BinaryTreeLevelOrderTraversalII:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack: List[TreeNode] = []
        stack.append(root)
        ans: List[List[int]] = []
        while stack:
            size = len(stack)
            levelnode: List[int] = []
            for i in range(size):
                node = stack.pop(0)
                levelnode.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            ans.insert(0,levelnode)

        return ans
