class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_val = float('inf')
        max_profit = 0

        for i in prices:
            min_val = min(min_val,i)
            max_profit = max(max_profit, i - min_val)
        return max_profit