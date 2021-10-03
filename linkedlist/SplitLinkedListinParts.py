"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.



Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.


Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
"""
from typing import List, Optional

from linkedlist.ListNode import ListNode


class SplitLinkedListinParts:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans: List[ListNode] = []
        cur = head
        allcount = 0
        while cur:
            allcount += 1
            cur = cur.next

        eachcount = allcount // k
        remainder = allcount - eachcount * k

        cur = ListNode(0)
        cur.next = head
        for i in range(k):
            if eachcount + remainder == 0:
                ans.append(None)
            else:
                tmp = eachcount
                while cur.next and tmp > 0:
                    cur = cur.next
                    tmp -= 1
                if remainder > 0:
                    if cur.next:
                        cur = cur.next
                    remainder -= 1

                temp = cur.next
                cur.next = None
                ans.append(head)
                head = temp
                cur = ListNode(0)
                cur.next = head # ensure cur is the tail element

        return ans
