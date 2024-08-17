#https://leetcode.com/problems/word-ladder/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neiDict = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                nei = word[:j] + "*" + word[j+1:]
                neiDict[nei].append(word)
        
        visited = set(beginWord)
        q = deque()
        q.append(beginWord)
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    neiPattern = word[:j] + "*" + word[j+1:]
                    for nei in neiDict[neiPattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res = res+1
        return 0
