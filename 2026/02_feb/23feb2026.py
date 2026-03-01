# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/submissions/1928950675

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        max_num = 2 ** k
        # print(max_num)
        buffer = {}

        current_val = 0
        for i in range(len(s)):
            current_bit = s[i]
            if i < k-1:
                # go thru this until k-1 bits
                current_val <<= 1
                current_val += int(current_bit)
            else:
                if i >= k:
                    bit_to_remove = int(s[i - k])
                    current_val -= (bit_to_remove << k-1)

                current_val <<= 1
                current_val += int(current_bit)
                if current_val < max_num:
                    buffer[current_val] = 1

            if len(buffer) >= max_num:
                # print(len(buffer))
                # print(buffer)
                return True
    
        return False

# Space complexity: O(2^k)
# Time complexity: O(n) where n is the length of s