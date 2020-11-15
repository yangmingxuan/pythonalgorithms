"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""
from btree.TreeNode import TreeNode


class CountCompleteTreeNodes:
    def countNodes(self, root: TreeNode) -> int:
        return self.countNodes(root.left) + self.countNodes(root.right) + 1 if root else 0

    def countNodes2(self, root: TreeNode) -> int:
        def getHeight(node: TreeNode) -> int:
            if not node:
                return 0
            return 1+getHeight(node.left)

        if not root:
            return 0
        left = getHeight(root.left)
        right = getHeight(root.right)

        if left == right:
            return 2**left+self.countNodes2(root.right)
        else:
            return 2**right+self.countNodes2(root.left)