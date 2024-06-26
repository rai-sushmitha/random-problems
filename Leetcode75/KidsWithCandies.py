#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find max
        max_val = max(candies)
        res = []
        for i in candies:
            if (i+extraCandies) < max_val:
                res.append(False)
            else:
                res.append(True)
        return res
