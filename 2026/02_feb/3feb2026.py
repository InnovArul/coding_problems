# https://leetcode.com/problems/trionic-array-i/submissions/1906239153

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        indicator = "S"
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1]) > 0:
                if indicator[-1] != 'I':
                    indicator += 'I'
            elif (nums[i] - nums[i-1]) < 0:
                if indicator[-1] != 'D':
                    indicator += 'D'
            else:
                return False

            # print(i, indicator)

            # allowed value: indicator = SIDI
            if len(indicator) > 4:
                # print(' greater than 4')
                return False

        return indicator == 'SIDI'

# Time complexity: O(n)
# Space complexity: O(1)