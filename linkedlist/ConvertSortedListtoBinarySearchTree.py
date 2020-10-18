"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

-10->-3->0->5->9
         |
        \/
        0
      /  \
    -3    9
    /    /
  -10   5

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]


Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5
"""
from btree import TreeNode
from linkedlist import ListNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        sorted_list = []
        while head:
            sorted_list.append(head.val)
            head = head.next

        def listToBST(l: int, r: int) -> TreeNode:
            if l > r:
                return None
            if l == r:
                return TreeNode(sorted_list[l])

            mid = (l+r) // 2
            node = TreeNode(sorted_list[mid])
            node.left = listToBST(l, mid-1)
            node.right = listToBST(mid+1, r)
            return node

        return listToBST(0, len(sorted_list)-1)
