class Solution:
    def climbStairs(self,n:int,costs:List[int])->int:
        dp=[0]*(n+1)
        for i in range(1,n+1):
            val=dp[i-1]+1
            if i>=2:
                val=min(val,dp[i-2]+4)
            if i>=3:
                val=min(val,dp[i-3]+9)
            dp[i]=val+costs[i-1]
        return dp[n]