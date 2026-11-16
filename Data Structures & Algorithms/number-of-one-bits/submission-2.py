class Solution:
    def hammingWeight(self, n: int) -> int:
        MASK = 0xFFFFFFFF
        n &= MASK
        ans = 0
        while n:
            ans += (n&1)
            n >>= 1
        return ans