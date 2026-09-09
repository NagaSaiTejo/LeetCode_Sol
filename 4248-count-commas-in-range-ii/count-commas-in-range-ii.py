class Solution:
    def countCommas(self, n: int) -> int:
        ans=0
        k=1000
        while k<=n:
            ans+=n-k+1
            if k>n//1000:
                break
            k*=1000
        return ans