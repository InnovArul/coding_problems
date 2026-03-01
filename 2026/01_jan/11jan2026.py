# https://leetcode.com/problems/maximal-rectangle/

import numpy as np

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # matrix = np.array(matrix).astype(int)
        
        # sum up heights
        self.allmax = -1
        rows, cols = len(matrix), len(matrix[0])

        heights = [0] * cols
        for row in matrix:
            for i in range(len(row)):
                if row[i] == "1": heights[i] += 1
                else: heights[i] = 0

            self.largestRectangeLeftRightBased(heights)
        
        return int(self.allmax)

    def largestRectangeLeftRightBased(self, histogram):
        n = len(histogram)
        left_smaller = [-1] * n
        right_smaller = [n] * n

        # find left smaller bar position
        for i in range(1, n):
            p = i - 1
            while p >= 0 and histogram[p] >= histogram[i]:
                p = left_smaller[p]
            
            left_smaller[i] = p

        # find right smaller bar position
        for i in range(n-2, -1, -1):
            p = i + 1
            while p < n and histogram[p] >= histogram[i]:
                p = right_smaller[p]
            
            right_smaller[i] = p

        for i in range(n):
            self.allmax = max(self.allmax, (right_smaller[i]-left_smaller[i]-1) * histogram[i])

    def largestRectangeQueueBased(self, histogram):
        buffer = []
        n = len(histogram)
        for j in range(n):
            currh = histogram[j]
            # do largest rectangle in histogram for every row
            # https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/629947248/
            if not buffer or buffer[-1][1] <= currh:
                # increasing heights are ok to append
                buffer.append((j, currh))
            else:
                # if a height less than last element is found,
                # pop all the elements until an element <= currh is found
                index = 0
                while buffer and buffer[-1][1] > currh:
                    index, height = buffer.pop()
                    self.allmax = max(self.allmax, height * (j - index))
                
                buffer.append((index, currh))

        while buffer:
            index, height = buffer.pop()
            self.allmax = max(self.allmax, height * (n - index))
