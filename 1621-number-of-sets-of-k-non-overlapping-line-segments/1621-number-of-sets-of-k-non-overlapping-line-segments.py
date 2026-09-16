class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod=1000000007
        return math.comb(n+k-1,2*k)%mod