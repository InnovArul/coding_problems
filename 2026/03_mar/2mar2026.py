# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/submissions/1936076496

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def findRightMostNumZeros(row):
            for i, element in reversed(list(enumerate(row))):
                if element == 1:
                    return n - 1 - i

            return n

        all_rows = []
        for i, row in enumerate(grid):
            all_rows.append(findRightMostNumZeros(row))
    
        swaps = 0
        print(all_rows)
        for i, num_zeros in enumerate(all_rows):
            # num_zeros should be >= current_expected_zeros
            curr_needed_zeros = n - 1 - i
            if all_rows[i] >= curr_needed_zeros: continue

            curr_count = all_rows[i]
            j = i + 1
            while j < n and curr_needed_zeros > all_rows[j]:
                all_rows[j], curr_count = curr_count, all_rows[j]

                swaps += 1
                j += 1
            
            # either j reached end or curr_needed_zeros <= all_rows[j]
            if j >= n: return -1
            all_rows[j] = curr_count
            swaps += 1
            

        return swaps

# Time Complexity: O(n^2)
# Space Complexity: O(n)
