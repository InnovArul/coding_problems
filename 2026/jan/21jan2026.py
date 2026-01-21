# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/description/

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if n % 2 == 0:
                res.append(-1)
            else:
                x = n - (((n+1) & -(n+1)) >> 1)
                res.append(x)
        
        return res