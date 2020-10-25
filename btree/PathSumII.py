"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
from typing import List

from btree import TreeNode


class PathSumII:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans: List[List[int]] = []
        eles: List[int] = []

        def path(node: TreeNode, currsum: int) -> None:
            if not node:
                return
            eles.append(node.val)
            if node.val == currsum and not node.left and not node.right:
                ans.append(list(eles))  # ans.append([x for x in eles])
            else:
                path(node.left, currsum-node.val)
                path(node.right, currsum-node.val)

            eles.pop()

        path(root, sum)
        return ans
