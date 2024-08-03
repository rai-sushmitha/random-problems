# https://leetcode.com/problems/trapping-rain-water/description/?envType=company&envId=google&favoriteSlug=google-six-months

class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height)-1
        L_Max, R_Max = height[L], height[R]

        water = 0

        while(L<R):
            if (L_Max < R_Max):
                L = L+1
                L_Max = max(L_Max, height[L])
                water = water + (L_Max - height[L])
            else:
                R =R-1
                R_Max = max(R_Max, height[R])
                water = water + (R_Max - height[R])

        return water
