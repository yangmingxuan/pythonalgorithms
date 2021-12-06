"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
from linkedlist import ListNode


class RemoveLinkedListElements:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        nxt = self.removeElements(head.next, val)
        if head.val == val:
            return nxt
        head.next = nxt
        return head

    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        firstNode = ListNode(0)
        firstNode.next = head
        pre, cur = firstNode, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return firstNode.next
