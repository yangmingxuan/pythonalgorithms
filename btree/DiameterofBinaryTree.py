"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100
"""
from typing import Optional

from btree.TreeNode import TreeNode


class DiameterofBinaryTree:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 1

        #The max distance to this node
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            ldia = dfs(node.left)
            rdia = dfs(node.right)

            self.max_diameter = max(self.max_diameter, ldia+rdia+1)

            return max(ldia, rdia) + 1

        dfs(root)

        return self.max_diameter - 1

