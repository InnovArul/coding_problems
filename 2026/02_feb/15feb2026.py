# https://leetcode.com/problems/add-binary/submissions/1919994219

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Store result digits (left-append for correct order)
        res = deque()

        def sumLastDigit(carry, d1, d2):
            carry = int(carry)
            # Base case: both strings exhausted
            if not (d1 or d2):
                if carry != 0: res.appendleft(carry)
                return

            # Extract last digit from each string (or 0 if empty)
            currd1 = int(d1[-1]) if len(d1) > 0 else 0
            currd2 = int(d2[-1]) if len(d2) > 0 else 0

            # Add digits with carry
            currsum = carry + currd1 + currd2
            res.appendleft(currsum % 2)  # Store result digit
            nextcarry = currsum // 2      # Propagate carry

            # Remove processed digits
            nextd1 = "" if len(d1) <= 1 else d1[:-1]
            nextd2 = "" if len(d2) <= 1 else d2[:-1]
            return sumLastDigit(nextcarry, nextd1, nextd2)

        sumLastDigit(0, a, b)
        return ''.join([str(d) for d in res])

# Time: O(max(len(a), len(b)))
# Space: O(max(len(a), len(b)))
