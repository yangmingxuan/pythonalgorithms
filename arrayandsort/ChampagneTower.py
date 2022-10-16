"""
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.



Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)



Example 1:

Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.
Example 2:

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
Example 3:

Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000


Constraints:

0 <= poured <= 10^9
0 <= query_glass <= query_row < 100
"""

class ChampagneTower:
    """
     Explanation: 每个杯子dp[r][c]装满后，都会分成两股向下一排的杯子流，其流向的杯子为dp[r+1][c]和dp[r+1][c+1]
     After each cup dp[r][c] is full, it will be divided into two flows of cups down to the next row, and the cups flowing to dp[r+1][c] and dp[r+1][c+ 1]
    """
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (query_row+2) for _ in range(query_row+2)]
        dp[0][0] = poured #Assume each glass catches all the champagne before dispensing it down

        for r in range(query_row+1):
            for c in range(r+1):
                flows = (dp[r][c] - 1) / 2 #Each glass can only hold 1, the rest flows to the next row
                if flows > 0:
                    dp[r+1][c] += flows
                    dp[r+1][c+1] += flows

        return min(1, dp[query_row][query_glass])