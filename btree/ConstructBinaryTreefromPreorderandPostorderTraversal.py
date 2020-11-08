"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.



Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""
from typing import List

from btree import TreeNode


class ConstructBinaryTreefromPreorderandPostorderTraversal:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        root = TreeNode(pre.pop(0))
        if root.val != post[0]:
            root.left = self.constructFromPrePost(pre, post)
        if root.val != post[0]:
            root.right = self.constructFromPrePost(pre, post)
        post.pop(0)
        return root

    def constructFromPrePost2(self, pre: List[int], post: List[int]) -> TreeNode:
        self.preindex, self.postindex = 0, 0

        def helper() -> TreeNode:
            root = TreeNode(pre[self.preindex])
            self.preindex += 1
            if root.val != post[self.postindex]:
                root.left = helper()
            if root.val != post[self.postindex]:
                root.right = helper()
            self.postindex += 1
            return root

        return helper();