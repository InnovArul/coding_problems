# https://leetcode.com/problems/trionic-array-ii/submissions/1908465814

from collections import deque
from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        # (type, sum, start_index, end_index)
        stack = deque([['S', 0, 0, 0]])
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if stack[-1][0] == 'I':
                    # add to sum
                    stack[-1][1] += nums[i]
                    # set end index
                    stack[-1][3] = i
                else:
                    stack.append(['I', nums[i]+nums[i-1], i-1, i])
            elif nums[i] < nums[i-1]:
                if stack[-1][0] == 'D':
                    # add to sum
                    stack[-1][1] += nums[i]
                    # set end index
                    stack[-1][3] = i
                else:
                    stack.append(['D', nums[i]+nums[i-1], i-1, i])
            else:
                if stack[-1][0] == 'E':
                    # add to sum
                    stack[-1][1] += nums[i]
                    # set end index
                    stack[-1][3] = i
                else:
                    stack.append(['E', nums[i]+nums[i-1], i-1, i])

        n = len(nums)
        maxEndingAt = [0] * n
        for i in range(n):
            maxEndingAt[i] = nums[i]
            if i > 0 and nums[i - 1] < nums[i]:
                maxEndingAt[i] += max(maxEndingAt[i - 1], nums[i-1])

        maxStartingAt = [0] * n
        for i in range(n - 1, -1, -1):
            maxStartingAt[i] = nums[i]
            if i < n - 1 and nums[i] < nums[i + 1]:
                maxStartingAt[i] += max(maxStartingAt[i + 1], nums[i+1])
    
        #print(maxStartingAt, maxEndingAt)
        # print(stack)
        ans = -float('inf')
        stack = list(stack) # Convert deque to list
        for a, b, c in zip(stack, stack[1:], stack[2:]):
            if a[0] == 'I' and b[0] == 'D' and c[0] == 'I':
                #print(a, b, c)
                #print(maxEndingAt[a[3]], b[1], maxStartingAt[c[2]], nums[a[3]], nums[b[3]])
                ans = max(ans, maxEndingAt[a[3]] + b[1] + maxStartingAt[c[2]] - nums[a[3]] - nums[b[3]])
        
        return ans

# Time complexity: O(n) for single pass to create stack and two passes to create maxStartingAt and maxEndingAt.
# Space complexity: O(n) for maxStartingAt and maxEndingAt arrays and O(n) for stack in worst case.