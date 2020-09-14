"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
from linkedlist import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None:
            return head
        cur: ListNode = head
        pre: ListNode = None
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1

        node: ListNode = pre
        tail: ListNode = cur
        tmp: ListNode = None
        while n > 0:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            n -= 1

        if node != None:
            node.next = pre
        else:
            head = pre

        tail.next = cur
        return head
