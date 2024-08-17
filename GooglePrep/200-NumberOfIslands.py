#https://leetcode.com/problems/number-of-islands/description/
class Solution:
    def getNeighbors(self, i,j, m, n):
        x = [[-1,0], [0, -1], [0, 1], [1, 0]]

        res = []

        for pt in x:
            if(0 <= pt[0]+i < m and 0 <= pt[1]+j < n):
                res.append((pt[0]+i, pt[1]+j))
        return res


    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid[i][j] = 0
                    q.append((i,j))
                    
                    while q:
                        val = q.popleft()
                        nei = self.getNeighbors(val[0],val[1], len(grid), len(grid[i]))
                        for n in nei:
                            if grid[n[0]][n[1]] == "1":
                                grid[n[0]][n[1]] = 0
                                q.append(n)
                    res += 1
        return res

# very efficient solution 
class Solution:
     def numIslands(self, grid: List[List[str]]) -> int:
        def foo(idx,idy):
            grid[idx][idy]='0'
            if idx-1>=0 and grid[idx-1][idy]=='1': foo(idx-1,idy)
            if idx+1<len(grid) and grid[idx+1][idy]=='1': foo(idx+1,idy)
            if idy-1>=0 and grid[idx][idy-1]=='1': foo(idx,idy-1)
            if idy+1<len(grid[0]) and grid[idx][idy+1]=='1': foo(idx,idy+1)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    foo(i,j)
                    count+=1
        return count
