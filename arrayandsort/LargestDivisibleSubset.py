"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.



Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
"""
from typing import List


class LargestDivisibleSubset:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        dp = [-1] * n

        def largestSubsetUtil(idx: int) -> int:
            if idx == n - 1:
                dp[idx] = 1
            if dp[idx] != -1:
                return dp[idx]
            ans = 0
            for i in range(idx+1, n):
                if nums[i] % nums[idx] == 0:
                    ans = max(ans, largestSubsetUtil(i))

            dp[idx] = ans+1
            return dp[idx]

        ans, ind = 0, 0
        for i in range(n):
            if dp[i] != -1:
                continue

            tmp = largestSubsetUtil(i)
            if ans < tmp:
                ans = tmp
                ind = i

        res = []
        res.append(nums[ind])
        i = ind + 1
        while i < n:
            if nums[i] % nums[ind] == 0:
                if dp[i] == dp[ind]-1:
                    res.append(nums[i])
                    ind = i
            i += 1

        return res

lds = LargestDivisibleSubset()
a = [1,2,4,8,3,6,9,12,18,36]
res = lds.largestDivisibleSubset(a)
print(res)
