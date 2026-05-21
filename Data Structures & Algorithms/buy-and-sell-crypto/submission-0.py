class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            v = prices[i]
            profit = max(profit, v - lowest)
            lowest = min(lowest, v)
        return profit