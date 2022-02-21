"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""
from typing import List


class ContiguousArray:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen, sum = 0, 0
        map = {}
        map[0] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                sum -= 1
            else:
                sum += 1
            if sum in map:
                #If there have been equal values before, it means that the sum from the next position to the current position is 0
                maxlen = max(maxlen, i - map[sum])
            else:
                map[sum] = i

        return maxlen
