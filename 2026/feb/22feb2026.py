# https://leetcode.com/problems/binary-gap/submissions/1927862499

class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        count = 0
        countstart = False
        while n > 0:
            if n & 1 == 1:
                # reset the count
                if countstart: count += 1
                ans = max(count, ans)
                count = 0
                countstart = True
            else:
                if countstart: count += 1

            n >>= 1
        
        return ans

# Space complexity: O(1)
# Time complexity: O(log(n)) where n is the input number