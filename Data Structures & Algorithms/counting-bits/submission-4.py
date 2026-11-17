class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        # 1100 - n
        # 1011 - n - 1
        # n&(n-1) = 1000
        for i in range(n+1):
            cnt_curr = 0
            while i:
                cnt_curr += 1
                i = i&(i-1)
            ans.append(cnt_curr)
        return ans