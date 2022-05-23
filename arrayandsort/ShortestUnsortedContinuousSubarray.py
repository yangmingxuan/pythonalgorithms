"""
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.



Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0


Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105


Follow up: Can you solve it in O(n) time complexity?
"""
from typing import List


class ShortestUnsortedContinuousSubarray:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right and nums[left] <= nums[left+1]:
            left += 1
        if left == right: #the array is sorted
            return 0

        while right > 0 and nums[right-1] <= nums[right]:
            right -= 1

        minx = min(nums[left:right+1])
        maxx = max(nums[left:right+1])

        tmp = 0
        while tmp < left and nums[tmp] <= minx: #find the min to left
            tmp += 1
        left = tmp

        tmp = len(nums)-1
        while tmp > right and nums[tmp] >= maxx: #find the max to right
            tmp -= 1
        right = tmp

        return right-left+1
