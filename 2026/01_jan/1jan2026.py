# https://leetcode.com/problems/plus-one/submissions/1871330177

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            digits[i] += carry
            carry = 0
            if digits[i] > 9:
                digits[i] = digits[i] % 10
                carry = 1

        if carry:
            digits = [1] + digits

        return digits