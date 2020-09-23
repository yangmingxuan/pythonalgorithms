"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
import sys
from typing import List


class MinimumSizeSubarraySum:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans = sys.maxsize
        sum, left = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                ans = min(ans, i+1-left)
                sum -= nums[left]
                left += 1
        return ans if ans != sys.maxsize else 0
