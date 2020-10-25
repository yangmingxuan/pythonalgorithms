"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from typing import List

from btree import TreeNode


class ConstructBinaryTreefromInorderandPostorderTraversal:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        valindex = {val:i for i, val in enumerate(inorder)}

        def helper(infrom: int, postfrom: int, length: int) -> TreeNode:
            if length == 0:
                return None
            rootval = postorder[postfrom+length-1]
            node = TreeNode(rootval)
            inorderindex = valindex[rootval]
            leftlen = inorderindex - infrom
            rightlen = length - 1 - leftlen

            node.left = helper(infrom, postfrom, leftlen)
            node.right = helper(infrom+leftlen+1, postfrom+leftlen, rightlen)
            return node

        def helper2(low:int, hight: int) -> TreeNode:
            if low > hight:
                return None
            rootval = postorder.pop();
            node = TreeNode(rootval)
            mid = valindex[rootval];
            node.right = helper2(mid+1, hight)
            node.left = helper2(low, mid-1)
            return node

        return helper2(0, len(postorder)-1)
        #return helper(0, 0, len(inorder))
