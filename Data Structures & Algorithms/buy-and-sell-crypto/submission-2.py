class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0, 1
        max_profit = 0

        while j < len(prices):
            buy = prices[i]
            sell = prices[j]

            if buy > sell:
                i = j
            else: 
                profit = sell - buy
                max_profit = max(max_profit, profit)
            j += 1
        
        return max_profit

        