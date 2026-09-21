class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res=[0]*k
        dp=[0]*k
        for x in nums:
            v=x%k
            nxt=[0]*k
            nxt[v]+=1
            for r in range(k):
                if dp[r]:
                    nxt[(r*v)%k]+=dp[r]
            dp=nxt
            for r in range(k):
                res[r]+=dp[r]
        return res