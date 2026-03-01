# https://leetcode.com/problems/maximum-matrix-sum/submissions/1875348453

import numpy as np

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        matrix = np.array(matrix)
        abs_matrix = np.abs(matrix)

        # find absolute sum of all elements in matrix
        abs_sum = abs_matrix.sum()

        # total number of negative elements
        negsign = (matrix < 0).sum()
        
        # if total neg numbers is even, we will be able to convert all of them to positive
        if negsign % 2 == 0:
            return int(abs_sum)
        else:
            # NOTE: min element is already part of abs_sum.
            # so, we have to subtract it twice before returning
            return int(abs_sum - 2 * abs_matrix.min())