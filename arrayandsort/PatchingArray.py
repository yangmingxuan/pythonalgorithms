"""
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.



Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums is sorted in ascending order.
1 <= n <= 231 - 1
"""
from typing import List


class PatchingArray:
    def minPatches(self, nums: List[int], n: int) -> int:
        max = 0
        count = 0
        for num in nums:
            """
            nums = [1,5,10], n = 20
            1 -> 1
            2 -> 1 + 2 = upto 3 - patch = 1
            3 -> already covered if we added 2 - no need to patch. as it is already covered
            4 -> 4 + 3 = upto 7 will be covered - patch = 2
            5 -> 5 + 7 = upto 12 will be covered
            6 - not requered already covered
            7, 8, 9 - already covered
            10 - its in the given array and 10 + 12 = upto 22 will be covered
            so minimum of 2 patches must be required
            """
            while num > max + 1:
                max += max + 1
                count += 1
                if max >= n:
                    return count
            #now num become < max, so add it as it will be covered
            max += num
            if max >= n:
                return count

        #if we reach here, we still didn't coverd the whole target so, repeat until we cover them
        while n > max + 1:
            max += max + 1
            count += 1

        return count

    #optimization
    def minPatches2(self, nums: List[int], n: int) -> int:
        max, count, i = 1, 0, 0
        while max <= n:
            if i < len(nums) and nums[i] <= max:
                max += nums[i]
                i += 1
            else:
                max *= 2
                count += 1

        return count
