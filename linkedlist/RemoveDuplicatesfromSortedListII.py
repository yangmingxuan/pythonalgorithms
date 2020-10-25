"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""
from linkedlist import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = ListNode(0)
        node.next = head
        pre, cur, nxt = node, head, head.next
        while nxt:
            rep = False
            while nxt and cur.val == nxt.val:
                rep = True
                nxt = nxt.next
            if rep:
                pre.next = nxt
                if not nxt:
                    break
                else:
                    cur = nxt
                    nxt = nxt.next
            else:
                pre = pre.next
                cur = cur.next
                nxt = nxt.next

        return node.next
