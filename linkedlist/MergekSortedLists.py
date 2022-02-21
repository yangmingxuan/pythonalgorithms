"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""
from typing import List, Optional

from linkedlist.ListNode import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
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

        def mergeKListWithIndex(l: int, r: int) -> ListNode:
            if l == r:
                return lists[l]
            m = (l+r) // 2
            lnode = mergeKListWithIndex(l, m)
            rnode = mergeKListWithIndex(m+1, r)
            return mergeTwoLists(lnode, rnode)

        return mergeKListWithIndex(0, len(lists)-1)
