"""
 4Sum II
 Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0


    Example 1:

    Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
    Output: 2
    Explanation:
    The two tuples are:
    1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
    Example 2:

    Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
    Output: 1


    Constraints:

    n == nums1.length
    n == nums2.length
    n == nums3.length
    n == nums4.length
    1 <= n <= 200
    -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28

"""
from typing import List


class FourSumII:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        twosum = {}
        for m in nums1:
            for n in nums2:
                if (m+n) not in twosum:
                    twosum[m+n] = 1
                else:
                    twosum[m+n] += 1

        for m in nums3:
            for n in nums4:
                if -(m+n) in twosum:
                    ans += twosum[-(m+n)]

        return ans
