"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
"""
from typing import List


class PairsofSongsWithTotalDurationsDivisibleby60:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return 0
        ans = 0
        timeDiv = {}
        for t in time:
            remainder = t % 60
            tdiv = 60 - remainder
            if tdiv == 60:
                tdiv = 0
            if tdiv in timeDiv:
                ans += timeDiv[tdiv]

            timeDiv[remainder] = timeDiv.setdefault(remainder, 0) + 1

        return ans

    def numPairsDivisibleBy602(self, time: List[int]) -> int:
        if not time:
            return 0
        ans = 0
        count = [0] * 60;
        for t in time:
            remainder = t % 60
            count[remainder] += 1

        #if remainder = 0 or 30 ans += C(count,2)
        ans += count[0] * (count[0] - 1) // 2
        ans += count[30] * (count[30] - 1) // 2
        for i in range(1, 30):
            ans += count[i] * count[60-i]

        return ans
