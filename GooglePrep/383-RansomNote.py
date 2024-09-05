#https://leetcode.com/problems/ransom-note/description/?envType=company&envId=google&favoriteSlug=google-thirty-days
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for c in ransomNote:
            if c not in magazine:
                return False

            idx = magazine.index(c)
            magazine = magazine[:idx] + magazine[idx+1:]
        return True
