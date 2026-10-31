class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD=10**9+7
        m,n=len(grid),len(grid[0])
        dp=[[0]*n for i in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 or dp[i][j]==0:
                    continue
                r,c,d=i,j+1,0
                while 0<=r<m and 0<=c<n and grid[r][c]==1:
                    r,c,d=(r+1,c,1) if d==0 else (r,c+1,0)
                if 0<=r<m and 0<=c<n:
                    dp[r][c]=(dp[r][c]+dp[i][j])%MOD
                r,c,d=i+1,j,1
                while 0<=r<m and 0<=c<n and grid[r][c]==1:
                    r,c,d=(r+1,c,1) if d==0 else (r,c+1,0)
                if 0<=r<m and 0<=c<n:
                    dp[r][c]=(dp[r][c]+dp[i][j])%MOD
        return dp[m-1][n-1]