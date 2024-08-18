# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

# Implemented solution 
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        numDict = {}

        i, j = 0, 0
        n = len(nums)
        res = 0

        while(j<n):
            if nums[j] in numDict.keys():
                if numDict[nums[j]] == k:
                    while(nums[i] != nums[j] and i<=j):
                        numDict[nums[i]] -= 1
                        i=i+1
                    i += 1
                        
                else:
                    numDict[nums[j]] += 1
            else:
                numDict[nums[j]] = 1
            res = max(res, j-i+1)
            # print(f"i : {i} , j : {j} , numDict : {numDict}, res : {res}")
            j=j+1
        
        res = max(res, j-i)
        return res


#Optimized clean solution
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        numDict = {}

        i, j = 0, 0
        n = len(nums)
        res = 0

        while(j<n):
            numDict[nums[j]] = numDict.get(nums[j], 0) + 1
            while(numDict[nums[j]] > k):
                numDict[nums[i]] -= 1
                i=i+1

            res = max(res, j-i+1)
            j=j+1
        
        return res
        
