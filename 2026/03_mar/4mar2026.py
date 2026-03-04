# https://leetcode.com/problems/special-positions-in-a-binary-matrix/submissions/1937206009

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        
        for row in range(m):
            for col in range(n):
                row_count[row] += mat[row][col]
                col_count[col] += mat[row][col]
        
        ans = 0
        for row in range(m):
            if row_count[row] == 1:
                for col in range(n):
                    if mat[row][col] == 1 and col_count[col] == 1:
                        ans += 1
                        break

        return ans

# Time complexity: O(m*n)
# Space complexity: O(m+n)
