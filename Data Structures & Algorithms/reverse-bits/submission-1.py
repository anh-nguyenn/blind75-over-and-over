class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            # extract most right bit
            bit = n & 1
            # update ans
            ans = (ans<< 1) | bit
            # shift left
            n >>= 1
        return ans
