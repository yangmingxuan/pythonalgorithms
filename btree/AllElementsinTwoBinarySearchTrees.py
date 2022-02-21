"""
  Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.



    Example 1:
      2            1
     / \          / \
    1   4        0   3

    Input: root1 = [2,1,4], root2 = [1,0,3]
    Output: [0,1,1,2,3,4]

    Example 2:
      1            8
       \          /
        8        1

    Input: root1 = [1,null,8], root2 = [8,1]
    Output: [1,1,8,8]


    Constraints:

    The number of nodes in each tree is in the range [0, 5000].
    -10^5 <= Node.val <= 10^5

"""
from collections import deque
from typing import List

from btree.TreeNode import TreeNode


class AllElementsinTwoBinarySearchTrees:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        tree1 = deque()
        tree2 = deque()
        node = root1
        while node:
            tree1.append(node)
            node = node.left

        node = root2
        while node:
            tree2.append(node)
            node = node.left

        while tree1 or tree2:
            #findtree1 = True
            if not tree2:
                #findtree1 = True
                tree = tree1
            elif not tree1:
                #findtree1 = False
                tree = tree2
            elif tree1[-1].val > tree2[-1].val:
                #findtree1 = False
                tree = tree2
            else:
                tree = tree1

            node = tree.pop()
            ans.append(node.val)
            if node.right:
                node = node.right
                while node:
                    tree.append(node)
                    node = node.left

        return ans
