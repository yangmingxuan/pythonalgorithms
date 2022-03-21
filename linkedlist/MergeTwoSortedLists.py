"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from linkedlist.ListNode import ListNode


class MergeTwoSortedLists:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lret = ListNode(0)
        ll, lr = l1, l2
        lptr = lret
        while ll and lr:
            if ll.val <= lr.val:
                lptr.next = ll
                ll = ll.next
            else:
                lptr.next = lr
                lr = lr.next
            lptr = lptr.next

        if ll:
            lptr.next = ll
        else:
            lptr.next = lr

        return lret.next

