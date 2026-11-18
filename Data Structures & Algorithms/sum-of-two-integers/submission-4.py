class Solution:
    def getSum(self, a: int, b: int) -> int:
        # xor: result without carry
        # &: carry
        # negative handle
        # 0x7FFFFFFF -> maximum positive
        MASK = 0xFFFFFFFF
        while a:
            tmp = (b^a)&MASK
            carry = ((b&a)<<1)&MASK
            b = tmp
            a = carry
        return b if b<0x7FFFFFFF else ~(b^MASK)

        # 0100
        # 0111
        # 0011 (XOR)
        # 0100 << 1 = 1000 
        # 1011