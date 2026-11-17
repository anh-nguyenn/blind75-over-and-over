class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        # 4 -> [0, 1, 2, 3] 011 -001
        for i in range(1, n + 1):
            
            ans[i] = ans[i>>1] + (i&1)
            print(ans[i], ans[i>>1], i&1)
        return ans