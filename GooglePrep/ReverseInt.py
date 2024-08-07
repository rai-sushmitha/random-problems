# https://leetcode.com/problems/reverse-integer/?envType=company&envId=google&favoriteSlug=google-thirty-days
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        isNeg = 1
        if x < 0:
            isNeg = -1
            x = x * -1
        while(x > 0):
            a = x%10
            res = res*10 + a
            x = x //10
        if (res > math.pow(2,31)):
            return 0
        
        return res*isNeg

