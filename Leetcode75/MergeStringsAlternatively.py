#https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i=0
        while(i<len(word1) and i<len(word2)):
            res+=word1[i]+word2[i]
            i=i+1
        while(i<len(word1)):
            res+=word1[i:len(word1)]
            break
        while(i<len(word2)):
            res+=word2[i:len(word2)]
            break
        return res
