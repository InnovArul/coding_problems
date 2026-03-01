#https://leetcode.com/problems/construct-the-minimum-bitwise-array-i

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n % 2 == 0:
                ans.append(-1)
            else:
                found = False
                for i in range(1, n):
                    if i | (i+1) == n:
                        ans.append(i)
                        found = True
                        break

                if not found: ans.append(-1)
        
        return ans