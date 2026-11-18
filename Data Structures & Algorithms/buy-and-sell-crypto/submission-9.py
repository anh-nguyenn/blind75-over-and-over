class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 # buy, sell
        profit = 0
        while right < len(prices):
            diff = prices[right] - prices[left]
            if diff >= 0: # earn profit
                profit = max(profit, diff)
            else: #meet a lower price to buy
                left = right
            right += 1
        return profit

