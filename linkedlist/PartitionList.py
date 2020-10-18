"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
from linkedlist import ListNode


class PartitionList:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        pre = ListNode()
        pre.next = head
        cur = head
        prefirst = pre
        head = pre
        firstGreater: ListNode = None
        while cur:
            if not firstGreater and cur.val >= x:
                firstGreater = cur
            if firstGreater and cur.val < x:
                prefirst.next = cur
                pre.next = cur.next
                cur.next = firstGreater
                prefirst = cur
                cur = pre.next
                continue
            pre = pre.next
            cur = cur.next
            if not firstGreater:
                prefirst = prefirst.next

        return head.next
