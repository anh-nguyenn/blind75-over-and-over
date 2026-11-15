class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MASK_INT = 0x7FFFFFFF
        while b != 0:
            tmp_ans = (a ^ b)&MASK
            carry = ((a&b) << 1)&MASK
            a = tmp_ans
            b = carry
        return a if a < MASK_INT else ~(a^MASK)