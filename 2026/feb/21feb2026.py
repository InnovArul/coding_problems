# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/submissions/1926741187

import math

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0

        def get_num1s(n):
            num1s = 0
            while n != 0:
                if n & 1: num1s += 1
                n >>= 1

            return num1s

        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            
            limit = int(math.sqrt(n)) + 1
            for i in range(3, limit, 2):  # check only odd numbers
                if n % i == 0:
                    return False
            
            return True


        for i in range(left, right+1):
            num1s = get_num1s(i)
            if is_prime(num1s):
                ans += 1
        
        return ans

# Space complexity: O(1)
# Time complexity: O(n * log(m)) where n is the number of integers in the range [left, right] and m is the maximum integer in that range (since we need to