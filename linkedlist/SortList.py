"""
Given the head of a linked list, return the list after sorting it in ascending order.



Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-10^5 <= Node.val <= 10^5


Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""
from typing import Optional

from linkedlist.ListNode import ListNode


class SortList:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeList(l1: ListNode, l2: ListNode) -> ListNode:
            tmp = ListNode(0)
            sortlist = tmp
            while l1 and l2:
                if l1.val < l2.val:
                    tmp.next = l1
                    l1 = l1.next
                    tmp = tmp.next
                else:
                    tmp.next = l2
                    l2 = l2.next
                    tmp = tmp.next
            if l1:
                tmp.next = l1
            elif l2:
                tmp.next = l2

            return sortlist.next

        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tmp = slow
        slow = slow.next
        tmp.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return mergeList(l1, l2)

