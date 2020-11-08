"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
from linkedlist.ListNode import ListNode


class RotateList:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head;
        pre , cur = head, head.next
        count = 1
        while cur:
            pre = cur
            cur = cur.next
            count += 1

        k %= count
        if k == 0:
            return head

        #let the link list to a loop
        pre.next = head
        cur = head

        #going counterclockwise k times equals going clockwise count-k times
        k = count - k
        while k > 0:
            pre =  cur
            cur = cur.next
            k -= 1

        pre.next = None
        return cur
