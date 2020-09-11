"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
import collections
from typing import List


class FindAllDuplicatesinanArray:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            nums[abs(num) - 1] *= -1
        return ans

    def findDuplicates2(self, nums: List[int]) -> List[int]:
        return list(k for k, v in collections.Counter(nums).items() if v == 2)
