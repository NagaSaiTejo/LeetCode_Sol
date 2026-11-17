class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n=len(s)
        cost=[[float('inf')]*n for i in range(n)]
        for length in range(1,n+1):
            divisors=[]
            for d in range(1,length):
                if length%d==0:
                    divisors.append(d)
            for i in range(n-length+1):
                j=i+length-1
                if length==1:
                    continue
                min_c=float('inf')
                sub=s[i:j+1]
                for d in divisors:
                    curr_c=0
                    parts=length//d
                    for p in range(d):
                        for x in range(parts//2):
                            if sub[p+x*d]!=sub[p+(parts-1-x)*d]:
                                curr_c+=1
                    min_c=min(min_c,curr_c)
                cost[i][j]=min_c
        
        dp=[[float('inf')]*(k+1) for i in range(n+1)]
        dp[0][0]=0
        for i in range(1,n+1):
            for j in range(1,min(i,k)+1):
                for p in range(j-1,i):
                    dp[i][j]=min(dp[i][j],dp[p][j-1]+cost[p][i-1])
        return dp[n][k]
        