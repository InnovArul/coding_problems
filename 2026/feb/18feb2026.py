# https://leetcode.com/problems/binary-number-with-alternating-bits/submissions/1922847694

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        expected_bit = None
        while n:
            last_bit = n & 1

            if expected_bit is None or last_bit == expected_bit:
                expected_bit = (last_bit + 1) % 2
                n >>= 1
            else:
                return False

        return True

# Space complexity: O(1) - only a few variables used
# Time complexity: O(log n) - we check each bit of n once