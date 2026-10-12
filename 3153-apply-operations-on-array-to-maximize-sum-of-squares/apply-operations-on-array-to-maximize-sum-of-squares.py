class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD=10**9+7
        c=[0]*31
        for x in nums:
            for i in range(31):
                if(x>>i)&1:
                    c[i]+=1
        arr=[0]*k
        for i in range(31-1,-1,-1):
            for j in range(k):
                if c[i]>0:
                    arr[j]|=(1<<i)
                    c[i]-=1
        ans=0
        for x in arr:
            ans=(ans+x*x)%MOD
        return ans