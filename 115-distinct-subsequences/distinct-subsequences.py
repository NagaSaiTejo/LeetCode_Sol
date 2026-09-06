class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(t)
        state_counts=[0]*(n+1)
        state_counts[0]=1
        for char in s:
            for j in range(n-1,-1,-1):
                if char==t[j]:
                    state_counts[j+1]+=state_counts[j]
        return state_counts[n]