#Runtime: 1285 ms, faster than 76.85% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.1 MB, less than 7.00% of Python3 online submissions for Best Time to Buy and Sell Stock.

#TODO: learning - today's price is either a buying point or a selling point.
# you don't need to return the buying day or the selling day, just the max_profit!!!!!!
# this is why doing O(n) search is possible: just keep track of max_profit and search for lower min_prices!!

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i]< min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit