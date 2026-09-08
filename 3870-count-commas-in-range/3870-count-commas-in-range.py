class Solution:
    def countCommas(self, n: int) -> int:
        ans=0
        thresh=1000
        while n>=thresh:
            ans+=n-thresh+1
            thresh*=1000
        return ans