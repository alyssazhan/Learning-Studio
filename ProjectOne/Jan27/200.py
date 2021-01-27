#https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols=len(grid),len(grid[0])
        res=0
        seen=[[False for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and not seen[r][c]:
                    # self.dfs(r,c,grid,seen,rows,cols)
                    self.bfs(r,c,grid,seen,rows,cols)
                    res+=1
        return res

    def bfs(self,r,c,grid,seen,rows,cols):
        seen[r][c]=True
        stack=[(r,c)]
        dire=[(1,0),(0,1),(-1,0),(0,-1)]
        while stack:
            r,c=stack.pop()
            for d in dire:
                nr,nc=d[0]+r,d[1]+c
                if self.isValid(nr,nc,grid,seen,rows,cols):
                    stack.append((nr,nc))
                    seen[nr][nc]=True

    def isValid(self,r,c,grid,seen,rows,cols):
        if r<0 or c<0 or r>=rows or c>=cols or seen[r][c] or grid[r][c]=='0':
            return False
        return True