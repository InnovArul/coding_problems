# https://leetcode.com/problems/champagne-tower/submissions/1918839548

class Solution:
    def champagneTower(self, p: int, qr: int, qg: int) -> float:
        
        @cache
        def excess(r, c):
            if c < 0 or c > r: return 0
            if r == 0 and c == 0:
                return 0 if p <= 0 else p - 1
            
            currfill = howmuch(r, c)
            if currfill > 1: return currfill -1
            return 0
            
            
        @cache 
        def howmuch(r, c):  
            if r == 0 and c == 0: return p
            currfill = 0.5 * excess(r-1, c-1) + 0.5 * excess(r-1, c)
            # print('howmuch', r, c, currfill)            
            return currfill
        
        hm = howmuch(qr, qg)
        return 1 if hm > 1 else hm

# Space complexity: O(n^2) where n is the number of rows in the tower, due to the caching of results for each glass.
# Time complexity: O(n^2) in the worst case, as we may need to compute the amount of champagne for each glass in the tower up to the specified row and glass.