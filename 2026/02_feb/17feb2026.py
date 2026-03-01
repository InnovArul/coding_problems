# https://leetcode.com/problems/binary-watch/submissions/1922639730

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hourbits = defaultdict(list)
        minbits = defaultdict(list)
        
        def countbits(n):
            res = 0
            while n>0:
                res += 1
                n = n & n-1
            
            return res
        
        for num in range(60):
            ones = countbits(num)
            if num < 12: hourbits[ones].append(f"{num}")
            minbits[ones].append(f"{num:02d}")
            
        res = []
        for hrbit in range(turnedOn+1):
            minbit = turnedOn - hrbit
            for hr in hourbits[hrbit]:
                for minn in minbits[minbit]:
                    res.append(hr+":"+minn)
                    
        return res

# Space: O(1) - 720 possible times
# Time: O(1) - 720 possible times
