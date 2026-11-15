class Solution:
    def getSum(self, a: int, b: int) -> int:
        # use hex because a and b is beyond binary range -128 to 127
        # a ^ b = result without carry
        # a & b = carry
        # we shift carry to left (<<1), we continue calculate ^ till our carry is 0
        # we have to MASK because we need to handle negative number and avoid infinite loop
        # to identify negative result, we use 0x7FFFFFFF
        # to flip all bits -> XOR with all 1. 
        MASK = 0xFFFFFFFF
        MAX_POSITIVE = 0x7FFFFFFF
        while b != 0:
            carry = ((a&b)<<1)&MASK
            a = (a^b)&MASK
            b = carry
        ans = a if a <= MAX_POSITIVE else ~(a^MASK)
        return ans
            