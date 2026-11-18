class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp =float('inf')
        profit = 0
        for i in range(len(prices)):
            # prices[i] prices at i day
            if prices[i] < minp:
                minp = prices[i] # if we find a lower price to buy, update it
            profit = max(profit, prices[i] - minp)
        return profit