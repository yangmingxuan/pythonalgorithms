"""
You are given a binary tree in which each node contains an integer value.

    Find the number of paths that sum to a given value.

    The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

    The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

    Example:

    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1

    Return 3. The paths that sum to 8 are:

    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11

"""
from typing import Optional

from btree.TreeNode import TreeNode


class PathSumIII:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        map = {}
        map[0] = 1

        def dfs(node: TreeNode, currSum: int) -> int:
            if not node:
                return 0
            count = 0

            currSum += node.val
            if (currSum-targetSum) in map:
                count += map[currSum-targetSum]

            if currSum in map:
                map[currSum] += 1
            else:
                map[currSum] = 1

            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)

            map[currSum] -= 1  #reset the value

            return count

        return dfs(root, 0)
