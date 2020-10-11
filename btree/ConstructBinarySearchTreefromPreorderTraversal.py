"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
              8
            /   \
           5    10
          / \     \
         1   7    12

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""
import sys
from typing import List

from btree import TreeNode


class ConstructBinarySearchTreefromPreorderTraversal:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder or len(preorder) == 0:
            return None

        self.idx, n = 0, len(preorder)

        def backtracking(lower: int, upper: int) -> TreeNode:
            if self.idx == n:
                return None
            val = preorder[self.idx]
            if val < lower or val > upper: #not this sub tree
                return None

            node: TreeNode = TreeNode(val)
            self.idx += 1
            node.left = backtracking(lower, val)
            node.right = backtracking(val, upper)
            return node

        return backtracking(-sys.maxsize-1, sys.maxsize)

