class Solution:
    def fib(self, n: int) -> int:
        memo={}
        def solve(k):
            if k<=1:
                return k
            if k in memo:
                return memo[k]
            memo[k]=solve(k-1)+solve(k-2)
            return memo[k]
        return solve(n)