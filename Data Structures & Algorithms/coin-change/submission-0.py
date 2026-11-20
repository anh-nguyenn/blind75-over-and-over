class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [float('inf')] * (amount+1)
        ans[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    ans[i] = min(ans[i], 1 + ans[i - coin])
        return ans[amount] if ans[amount] != float('inf') else -1