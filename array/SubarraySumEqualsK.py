"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2


Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
from typing import List


class SubarraySumEqualsK:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        # map saves all the sum from nums[0] to nums[i]
        map = {}
        map[0] = 1
        for num in nums:
            sum += num
            if (sum - k) in map:
                #sum - k ==  a sum from nums[0] to nums[j] means there is a subarray(from j+1 to i) whose sum equals to k
                count += map.get(sum - k)
            map[sum] = map.setdefault(sum, 0) + 1
        return count
