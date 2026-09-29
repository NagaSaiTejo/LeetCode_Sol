class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m,n=len(grid),len(grid[0])
        if (m+n-1)%2!=0 or grid[0][0]==')' or grid[m-1][n-1]=='(':
            return False 
        max_bal=(m+n-1)//2
        visited=[[[False]*(max_bal+1) for j in range(n)] for i in range(m)]
        queue=collections.deque([(0,0,1)])
        visited[0][0][1]=True 
        while queue:
            r,c,bal=queue.popleft()
            if r==m-1 and c==n-1 and bal==0:
                return True 
            for nr,nc in ((r+1,c),(r,c+1)):
                if nr<m and nc<n:
                    nbal=bal+(1 if grid[nr][nc]=='(' else -1)
                    if 0<=nbal<=max_bal and not visited[nr][nc][nbal]:
                        visited[nr][nc][nbal]=True 
                        queue.append((nr,nc,nbal))
        return False 