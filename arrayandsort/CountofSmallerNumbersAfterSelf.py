"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].



    Example 1:

    Input: nums = [5,2,6,1]
    Output: [2,1,1,0]
    Explanation:
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.
    Example 2:

    Input: nums = [-1]
    Output: [0]
    Example 3:

    Input: nums = [-1,-1]
    Output: [0,0]


    Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

"""
from typing import List


class CountofSmallerNumbersAfterSelf:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def binarysearch(q: List[int], val: int) -> int:
            l, r = 0, len(q) - 1
            while l <= r:
                mid = (l+r) // 2
                if q[mid] < val:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        ans = []
        q = []
        for i in range(len(nums)-1, -1, -1):
            idx = binarysearch(q, nums[i])
            ans.append(idx)
            q.insert(idx, nums[i])

        return ans[::-1]
