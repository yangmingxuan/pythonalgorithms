"""
MatchstickstoSquare
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.



Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.


Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 10^8
"""
from typing import List


class MatchstickstoSquare:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks or len(matchsticks) < 4:
            return False

        allLength = sum(matchsticks)
        if allLength % 4 != 0:
            return False
        sideLength = allLength // 4

        matchsticks.sort(reverse=True)
        visited = [False] * len(matchsticks)

        def dfs(remain: int, sideidx: int) -> bool:
            if sideidx == 4:
                return True

            i = 0
            while i < len(matchsticks):
                if visited[i]:
                    i += 1
                    continue  #used
                if matchsticks[i] > remain:
                    return False  #cannot used to be linked to a stick

                visited[i] = True
                if remain == matchsticks[i]:
                    ans = dfs(sideLength, sideidx+1)
                else:
                    ans = dfs(remain - matchsticks[i], sideidx)
                visited[i] = False  #reset
                if ans:
                    return True

                while i+1 < len(matchsticks) and matchsticks[i+1] == matchsticks[i]:
                    i += 1
                i += 1

            return False

        return dfs(sideLength, 0)

mss = MatchstickstoSquare()
sticks = [100,100,100,100,100,100,100,100,4,100,2,2,100,100,100]
res = mss.makesquare(sticks)
print(res)
