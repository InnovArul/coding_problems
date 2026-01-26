# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = arr[1] - arr[0]
        mindiff_arr = [(arr[0], arr[1])]

        for i in range(2, len(arr)):
            currdiff = arr[i] - arr[i-1]
            if currdiff < mindiff:
                mindiff = currdiff
                mindiff_arr = [(arr[i-1], arr[i])]
            elif currdiff == mindiff:
                mindiff_arr.append((arr[i-1], arr[i]))
    
        return mindiff_arr
    
# Time Complexity: O(N log N) due to sorting
# Space Complexity: O(1) if we don't count the output list