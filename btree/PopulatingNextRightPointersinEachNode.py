"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example 1:
          1                      1
        /   \                  /    \
       2     3                2----->3-->NULL
      / \   / \              / \    / \
     4  5  6   7            4-->5->6-->7-->NULL


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000


Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""
from collections import deque


class PopulatingNextRightPointersinEachNode:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        if root.left:
            root.left.next = root.right
        if root.right:
            root.right.next = root.next.left if root.next else None

        self.connect(root.left)
        self.connect(root.right)
        return root

    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = deque()
        queue.appendleft(root)

        while queue:
            prev = None
            size = len(queue)
            for i in range(size):
                node = queue.pop()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

        return root
