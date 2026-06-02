class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_buy = prices[0]
        for sell in prices:
            if sell - best_buy > max_profit:
                max_profit = sell - best_buy
            if sell < best_buy:
                best_buy = sell
        return max_profit