# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles

class Rect:
    def __init__(self, bottomleft, topright):
        self.bottomleft = bottomleft
        self.topright = topright
    
    @property
    def bottomleft_x(self):
        return self.bottomleft[0]

    @property
    def bottomleft_y(self):
        return self.bottomleft[1]

    @property
    def topright_x(self):
        return self.topright[0]

    @property
    def topright_y(self):
        return self.topright[1]

    def iswithin(self, x, y, v):
        return x <= v <= y or y <= v <= x

    def isInside(self, pt):
        if (self.iswithin(self.bottomleft_x, self.topright_x, pt[0])
            and self.iswithin(self.bottomleft_y, self.topright_y, pt[1])):
                return True
        
        return False
    
    def getCorners(self):
        return (self.bottomleft, (self.bottomleft_x, self.topright_y),
                (self.topright_x, self.bottomleft_y), self.topright)

    def anyPointsInside(self, rect):
        isinside = False
        for pt in rect.getCorners():
            isinside = isinside or self.isInside(pt)
        
        return isinside

    def __str__(self):
        return f"rect(({self.bottomleft}),({self.topright}))"

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        maxarea = 0
        for rect1, rect2 in combinations(zip(bottomLeft, topRight), 2):
            rect1 = Rect(*rect1)
            rect2 = Rect(*rect2)
            maxarea = max(maxarea, self.intersectionSquareArea(rect1, rect2))
        
        return maxarea

    def intersectionSquareArea(self, r1, r2):
        """
        Compute area of intersection between two rectangles.
        Each rectangle: (bottom_x, bottom_y, top_x, top_y)
        """
        # Overlap in X
        overlap_width = max(0, min(r1.topright_x, r2.topright_x) - max(r1.bottomleft_x, r2.bottomleft_x))
        # Overlap in Y
        overlap_height = max(0, min(r1.topright_y, r2.topright_y) - max(r1.bottomleft_y, r2.bottomleft_y))

        return min(overlap_width, overlap_height) ** 2