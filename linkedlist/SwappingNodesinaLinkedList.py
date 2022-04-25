"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 100
"""
from typing import Optional

from linkedlist.ListNode import ListNode


class SwappingNodesinaLinkedList:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr, kthnode, antikthnode = head, head, head
        idx = 1
        while idx < k:
            ptr = ptr.next
            idx += 1

        #now the ptr is the kth node
        kthnode = ptr

        #Because the gap between antikthnode and ptr.next is now k,
        #if both move forward at the same time, when ptr reaches the end, antikthnode will be the kth node from the end.
        while ptr.next:
            ptr = ptr.next
            antikthnode = antikthnode.next

        kthnode.val, antikthnode.val = antikthnode.val, kthnode.val
        return head
