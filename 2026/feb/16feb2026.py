# https://leetcode.com/problems/reverse-bits/submissions/1921405186

class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0: return 0

        bins = []
        while n != 0:
            bins.append(n % 2)
            n //= 2
        
        # make it 32 bit
        filled_bits = f"{''.join([str(c) for c in bins]):0<32}"
        filled_bits = filled_bits.lstrip('0')
        return int(filled_bits, 2)

# Space complexity: O(1)
# Time complexity: O(1)
