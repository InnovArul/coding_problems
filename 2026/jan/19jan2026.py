# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        self.calcPrefixSum(mat)
        # print(self.prefixsum)
        
        m, n = len(mat), len(mat[0])
        print(m, n)
        low = 0
        high = min(m, n) + 1
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            print(low, high, mid, self.isSumLessThanOrEqToThreshold(mid, threshold))
            if self.isSumLessThanOrEqToThreshold(mid, threshold):
                answer = mid
                low = mid + 1
            else: 
                high = mid - 1
            print("after", low, high, mid, answer)

        return answer


    def calcPrefixSum(self, mat):
        m, n = len(mat), len(mat[0])
        self.prefixsum = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.prefixsum[i][j] = mat[i][j]
                if i > 0:
                    self.prefixsum[i][j] += self.prefixsum[i-1][j]
                
                if j > 0:
                    self.prefixsum[i][j] += self.prefixsum[i][j-1]
                
                if i > 0 and j > 0:
                    self.prefixsum[i][j] -= self.prefixsum[i-1][j-1]

            # print(i, self.prefixsum[i])

    def isSumLessThanOrEqToThreshold(self, side, thresh):
        if side == 0: return True
        m, n = len(self.prefixsum), len(self.prefixsum[0])

        for i in range(side-1, m):
            for j in range(side-1, n):
                currsum = self.prefixsum[i][j]
                if i >= side:
                    currsum -= self.prefixsum[i-side][j]
                if j >= side:
                    currsum -= self.prefixsum[i][j-side]
                
                if i >= side and j >= side:
                    currsum += self.prefixsum[i-side][j-side]
                
                # print(side, i, j, currsum)
                if currsum <= thresh:
                    return True
        
        return False