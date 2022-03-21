"""
    In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

    We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

    Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

    If it cannot be done, return -1.



    Example 1:
    tops = [2,1,2,4,2,2]
    bottoms = [5,2,6,2,3,2]

    rotate the 2nd and 4th(swap tops[1]bottoms[1] and tops[3]bottoms[3):
    tops = [2,2,2,2,2,2]
    bottoms = [5,1,6,4,3,2]


    Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
    Output: 2
    Explanation:
    The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
    If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
    Example 2:

    Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
    Output: -1
    Explanation:
    In this case, it is not possible to rotate the dominoes to make one row of values equal.


    Constraints:

    2 <= tops.length <= 2 * 10^4
    bottoms.length == tops.length
    1 <= tops[i], bottoms[i] <= 6

"""
#from collections import Counter
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        topCount = [0] * 6
        bottomCount = [0] * 6
        sameCount = [0] * 6
        ans = n + 1

        for val in tops:
            topCount[val-1] += 1

        for i in range(n):
            bottomCount[bottoms[i]-1] += 1
            if tops[i] == bottoms[i]:  #Swapping values is meaningless if the values are the same
                sameCount[tops[i]-1] += 1

        for i in range(6):
            if topCount[i] + bottomCount[i] - sameCount[i] >= len(tops):
                ans = min(ans, min(topCount[i], bottomCount[i])-sameCount[i])

        return -1 if ans == n+1 else ans

        """
        topCount = Counter(tops)
        bottomCount = Counter(bottoms)
        sameCount = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

        for i in range(len(tops)):
            if tops[i] == bottoms[i]:
                sameCount[tops[i]] += 1

        ans = len(tops)+1
        for i in range(1,7):
            if i in topCount and i in bottomCount and topCount[i] + bottomCount[i] - sameCount[i] >= len(tops):
                ans = min(ans, min(topCount[i], bottomCount[i])-sameCount[i])

        return -1 if ans == len(tops)+1 else ans
        """
