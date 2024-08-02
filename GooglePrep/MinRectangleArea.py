https://leetcode.com/problems/minimum-area-rectangle/submissions/1342212315/?envType=company&envId=google&favoriteSlug=google-six-months
https://www.youtube.com/watch?v=fNksXUUyGyY

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()

        for x, y in points:
            points_set.add((x,y))

        min_area = float('inf')

        for (x1, y1) in points_set:
            for (x2,y2) in points_set:
                if(x1 == x2 or y1 == y2):
                    continue
                if((x1, y2) in points_set and (x2, y1) in points_set):
                    min_area = min(abs(x2-x1)*abs(y2-y1), min_area)

        return 0 if min_area == float('inf') else min_area
        
