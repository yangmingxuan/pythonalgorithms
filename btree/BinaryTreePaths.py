"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
from typing import List

from btree import TreeNode


class BinaryTreePaths:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans: List[str] = []
        path: List[str] = []

        def dfs(node: TreeNode):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append('->'.join(path))
            else:
                dfs(node.left)
                dfs(node.right)
            path.pop()

        dfs(root)
        return ans
