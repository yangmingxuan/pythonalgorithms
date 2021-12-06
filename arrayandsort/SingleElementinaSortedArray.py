"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
"""
from typing import List


class SingleElementinaSortedArray:
    """
    Solution must run in O(log n) time and O(1) space. So, binary search
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        while lo <= hi:
            mid = (lo+hi) // 2
            if mid == 0 or mid == len(nums) - 1:
                #nothing else
                return nums[mid]
            elif nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                #the single number
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    #the single number must be in the right part
                    lo = mid + 2
                else:
                    #the single number must be in the left part
                    hi = mid - 2
            else:
                if nums[mid] == nums[mid-1]:
                    lo = mid + 1
                else:
                    hi = mid - 1


