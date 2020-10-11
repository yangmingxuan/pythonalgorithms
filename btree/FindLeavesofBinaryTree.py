"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.



Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]


Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         /
        2


2. Now removing the leaf [2] would result in this tree:

          1


3. Now removing the leaf [1] would result in the empty tree:

          []
[[3,5,4],[2],[1]], [[3,4,5],[2],[1]], etc, are also consider correct answers since per each level it doesn't matter the order on which elements are returned.
"""
from typing import List

from btree import TreeNode


class FindLeavesofBinaryTree:
    """
     * null is level 0, leaf node is level 1, its parent is level 2, and so on
     * @param root
     * @return
     """
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        ans: List[List[int]] = []
        def helper(node: TreeNode) -> int:
            if not node:
                return 0
            level = 1 + max(helper(node.left), helper(node.right))
            if len(ans) < level:
                ans.append([])
            ans[level-1].append(node.val)
            return level

        helper(root)
        return ans
