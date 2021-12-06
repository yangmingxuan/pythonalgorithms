"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.



Example 1:

         3
        / \
       2   3
        \   \
         3   1

Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

         3
        / \
       4   5
      / \   \
     1   3   1

Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


Constraints:

The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^4
"""
from typing import Optional, List

from btree.TreeNode import TreeNode


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        * Record dp with int[2],
        * the first element record node and grandson node's max value,
        * the second element record the children's max value

        :param node:
        :return:int[2]
        """
        def backtrack(node: TreeNode) -> List[int]:
            if not node:
                return [0,0]
            leftdp = backtrack(node.left)
            rightdp = backtrack(node.right)

            #dp = []
            #dp[0] node.val+leftdp[1]+rightdp[1]
            #dp[1] max(leftdp)+max(rightdp)

            return [node.val+leftdp[1]+rightdp[1], max(leftdp)+max(rightdp)]

        return max(backtrack(root))

    def rob2(self, root: Optional[TreeNode]) -> int:
        dp = {}
        """
        Record dp with map
        :param node:
        :return: node's max value
        """
        def rob_max(node: TreeNode) -> int:
            if not node:
                return 0
            if node in dp:
                return dp[node]

            robcount = node.val
            if node.left:
                robcount += (rob_max(node.left.left) + rob_max(node.left.right))

            if node.right:
                robcount += (rob_max(node.right.left) + rob_max(node.right.right))

            robcount = max(robcount, rob_max(node.left)+rob_max(node.right))
            dp[node] = robcount

            return robcount

        return rob_max(root)
