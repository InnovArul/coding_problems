# 2483. Minimum Penalty for a Shop
# https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        bestTime = 0
        minPenalty = 0
        prefix = 0

        for i in range(len(customers)):
            # we move the closing time from 0 to n-1
            # if the customer is 'Y', we decrease the penalty by 1 (since they are served)
            # if the customer is 'N', we increase the penalty by 1 (since there is no customer)
            prefix += -1 if customers[i] == 'Y' else 1

            if prefix < minPenalty:
                bestTime = i + 1
                minPenalty = prefix

        return bestTime

# Time Complexity: O(n)
# Space Complexity: O(1)