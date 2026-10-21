class Solution:
    def minOperations(self, s: str) -> int:
        if list(s)==sorted(s):
            return 0 
        n=len(s)
        if n==2:
            return -1 
        mn=min(s)
        mx=max(s)
        if s[0]==mn or s[-1]==mx:
            return 1 
        if mn not in s[:n-1] and mx not in s[1:]:
            return 3 
        return 2