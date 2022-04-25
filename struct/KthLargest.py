"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:

1 <= k <= 10^4
0 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 10^4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""
import sys
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

        if k <= len(self.nums):
            self.kthElement = self.nums[k-1]
        elif self.nums:
            self.kthElement = self.nums[-1]
        else:
            self.kthElement = -sys.maxsize

    def add(self, val: int) -> int:
        def getIndex(left: int, right: int) -> int:
            while left < right:
                mid = (left+right) // 2
                mv = self.nums[mid]
                if mv == val:
                    return mid
                if mv > val:
                    left = mid + 1
                else:
                    right = mid
            return left

        if val < self.kthElement:
            if self.k > len(self.nums):
                self.nums.append(val)
                self.kthElement = val
            return self.kthElement

        idx = getIndex(0, min(self.k-1,len(self.nums)-1))
        self.nums.insert(idx, val)
        self.kthElement = self.nums[self.k-1]
        return self.kthElement
