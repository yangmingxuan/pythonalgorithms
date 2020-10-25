"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.



Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]


Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""
from typing import List

from btree import TreeNode


class DeleteNodesAndReturnForest:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root or not to_delete:
            return []
        ans: List[TreeNode] = []
        todelete = {x for x in to_delete}

        def dfs(node: TreeNode):
            if not node:
                return
            if node.left:
                dfs(node.left)
                if node.left.val in todelete:
                    node.left = None
                elif node.val in todelete:
                    ans.append(node.left)

            if node.right:
                dfs(node.righ)
                if node.right.val in todelete:
                    node.right = None
                elif node.val in todelete:
                    ans.append(node.right)

        if root.val not in todelete:
            ans.append(root)
        dfs(root)
        return ans
