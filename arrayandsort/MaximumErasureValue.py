"""

You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).



Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
"""
from typing import List


class MaximumErasureValue:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uniquedict = {}
        l, r, n, ans = 0, 0, len(nums), 0
        currsum = 0
        for r in range(n):
            currsum += nums[r]
            if nums[r] not in uniquedict or uniquedict[nums[r]] == 0:
                uniquedict[nums[r]] = 1
            else:
                uniquedict[nums[r]] += 1
                while uniquedict[nums[r]] != 1:
                    currsum -= nums[l]
                    uniquedict[nums[l]] -= 1
                    l += 1
            ans = max(ans, currsum)

        return ans
