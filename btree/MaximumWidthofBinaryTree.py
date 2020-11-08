"""
Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Constraints:

The given binary tree will have between 1 and 3000 nodes.
"""
from typing import List

from btree import TreeNode


class MaximumWidthofBinaryTree:
    """
    This is the algorithm of DFS, the BFS one in the JAVA project
    """
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maxwidth = 0

        def dfs(node: TreeNode, level: int, index: int, headings: List[int]):
            if not node:
                return
            if level == len(headings):
                headings.append(index)  #record the first index in this level

            self.maxwidth = max(self.maxwidth, index - headings[level] + 1)
            dfs(node.left, level + 1, 2 * index, headings)
            dfs(node.right, level + 1, 2 * index + 1, headings)

        headings = []
        dfs(root, 0, 0, headings)
        return self.maxwidth
