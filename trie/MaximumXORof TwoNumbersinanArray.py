"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.



Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127


Constraints:

1 <= nums.length <= 2 * 10^5
0 <= nums[i] <= 2^31 - 1
"""
from typing import List

class TrieBit:
    bits = None

    def __init__(self):
        self.bits = [None] * 2

class MaximumXORofTwoNumbersinanArray:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieBit()
        ans = 0
        for num in nums:
            # insert the num(binary mode) in to trie
            node = root
            for i in range(30, -1, -1): # from 30 to 0
                ithbit = (num>>i)&1  #the ith bit of num
                if node.bits[ithbit] is None:
                    node.bits[ithbit] = TrieBit()
                node = node.bits[ithbit]

            #find the max xor value
            node = root
            curmax = 0
            for i in range(30, -1, -1):  # from 30 to 0
                ithbit = (num >> i) & 1  # the ith bit of num
                wanttoxorbit = 1 - ithbit  #xor the other bit always bigger 0->1 or 1->0
                if node.bits[wanttoxorbit] is None:
                    wanttoxorbit = ithbit  #if not exist other bit, only choose the same bit
                curmax = (curmax << 1) | (wanttoxorbit ^ ithbit)
                node = node.bits[wanttoxorbit]

            ans = max(ans, curmax)

        return ans


