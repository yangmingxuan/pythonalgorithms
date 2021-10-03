"""
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional

from linkedlist.ListNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newone = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newone

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newone = head
        cur,pre = head,None
        while head:
            cur = head.next
            newone = head
            head.next = pre
            pre = head
            head = cur
        return newone
