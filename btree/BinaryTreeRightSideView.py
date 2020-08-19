"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
from collections import deque
from typing import List, Any

from btree import TreeNode


class BinaryTreeRightSideView:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        ans = []
        def backtrack(node: TreeNode, level: int) -> None:
            if level == len(ans):
                ans.append(node.val)

            for child in [node.right, node.left]:
                if child:
                    backtrack(child, level + 1)


        backtrack(root, 0)
        return ans

    def rightSideView2(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        ans: List[int] = []
        queue = deque([root,])

        while queue:
            levelcount = len(queue)
            for i in range(levelcount):
                node = queue.popleft()
                if i == 0:
                    # the first one means the rightest one
                    ans.append(node.val)
                
                for child in [node.right, node.left]:
                    if child:
                        queue.append(child)
                        
        return ans

