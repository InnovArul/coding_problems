# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        changed = True

        while changed:
            adjsums = []
            changed = False
            for i in range(1, len(nums)):
                adjsums.append(nums[i] + nums[i-1])
                changed = changed or (nums[i] < nums[i-1])

            #print(nums, adjsums, changed)
            if changed:
                # find the least sum
                index = 0
                for i in range(1, len(adjsums)):
                    if adjsums[i] < adjsums[index]:
                        index = i
                
                #print(index)
                nums[index] = adjsums[index]
                del nums[index+1]
                res += 1
            else:
                break

        return res