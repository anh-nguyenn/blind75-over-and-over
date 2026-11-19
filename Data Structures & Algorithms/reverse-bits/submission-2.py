class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        # for each i, we shift accordingly
        for i in range(32):
            # bit at i position
            bit = (n >> i)&1
            ans = ans | (bit<<(31-i))
        return ans