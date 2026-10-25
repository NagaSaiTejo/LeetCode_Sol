class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def fill(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=0:
                return 
            grid[r][c]=1 
            fill(r-1,c)
            fill(r+1,c)
            fill(r,c-1)
            fill(r,c+1)
        for i in range(rows):
            for j in range(cols):
                if (i==0 or i==rows-1 or j==0 or j==cols-1) and grid[i][j]==0:
                    fill(i,j)
        ans=0 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    ans+=1 
                    fill(i,j)
        return ans