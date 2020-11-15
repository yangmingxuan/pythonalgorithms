"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.



Example 1:
            2
           / \
          1   3

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:
              5
             / \
            3   6
           / \
          2   4
         /
        1

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.


Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
"""
import sys

from btree.TreeNode import TreeNode


class InorderSuccessorinBST:
    """
     * BST's feature left < parent < right, if p has right sub tree, its right sub tree's most lest leaf node is the answer,
     * else the answer is the inorder traversal's next node
    """
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        #set a pre_value variable, initialize it to the minimum, when we traverse the tree via inorder to a node
        #and its pre_value is p, this node is the answer
        preValue = -sys.maxsize-1
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if preValue == p.val:
                return node
            preValue = node.val
            node = node.right
        return None

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        curr, ancestor = root, None
        while curr.val != p.val:
            if p.val <curr.val:
                ancestor = curr
                curr = curr.left
            else:
                curr = curr.right

        return ancestor
