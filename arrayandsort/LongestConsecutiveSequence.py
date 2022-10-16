"""

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class LongestConsecutiveSequence:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        allnum = set(nums)

        for num in allnum:
            if num-1 in allnum: #cal before
                continue

            eachcount = 1
            num += 1
            while num in allnum:
                eachcount += 1
                num += 1

            longest = max(longest, eachcount)

        return longest

    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        longest, eachcount = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                eachcount += 1
            else:
                longest = max(longest, eachcount)
                eachcount = 1

        return max(longest, eachcount)
