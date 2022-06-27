"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
"""
from typing import List


class KthLargestElementinanArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(start: int, end: int) -> int:
            if start >= end:
                return nums[-k]
            basic = nums[(start+end)//2]
            i, j = start, end
            while i <= j:
                while i <= j and nums[i] < basic:
                    #if left is less than basic, it do not need swap
                    i += 1
                while i <= j and nums[j] > basic:
                    #if right is bigger than basic, do not need swap
                    j -= 1

                if i <= j:
                    #swap less to the left and bigger to the right
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            if len(nums) - k >= i:
                #it means the kth largest element is in the right
                return quicksort(i, end)
            if len(nums) - k <= j:
                # it means the kth largest element is in the left
                return quicksort(start, j)

            return nums[-k]

        return quicksort(0, len(nums)-1)

