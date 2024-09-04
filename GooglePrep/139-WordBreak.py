class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:
    def __init__(self):
        self.root = TreeNode()

    def Insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()

        for word in wordDict:
            trie.Insert(word)

        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            node=trie.root
            for j in range(i, n):
                c = s[j]
                if c not in node.children:
                    break
                node = node.children[c]
                if node.endOfWord:
                    dp[j+1]=True            
            
        return dp[n]
