"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5
"""
from typing import List


class BestTimetoBuyandSellStockIII:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minprice = prices[0]
        maxprofit = 0
        profit = [0] * n

        #Find largest profit one could make selling on any given day
        for i in range(n):
            minprice = min(minprice, prices[i])
            maxprofit = max(maxprofit, prices[i] - minprice)

            profit[i] = maxprofit #record the max profit in the ith day

        futuremaxprice = prices[-1]
        #Find largest profit on could make if stock be bought on a specific day and sold in the future
        for i in range(n-1, -1, -1):
            futuremaxprice = max(futuremaxprice, prices[i])
            profit[i] = max(profit[i], (futuremaxprice-prices[i])+profit[i])

            maxprofit = max(maxprofit, profit[i])

        return maxprofit

    def maxProfit2(self, prices: List[int]) -> int:
        t1min,t2min = prices[0], prices[0]
        t1profit, t2profit = 0, 0
        for price in prices:
            #the maximum profit if only one transaction is allowed
            t1min = min(t1min, price)
            t1profit = max(t1profit, price-t1min)

            #reinvest the gained profit in the second transaction
            t2min = min(t2min, price-t1profit)
            t2profit = max(t2profit, price-t2min)

        return t2profit

