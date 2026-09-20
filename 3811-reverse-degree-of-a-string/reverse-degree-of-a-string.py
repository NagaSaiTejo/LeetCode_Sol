class Solution:
    def reverseDegree(self, s: str) -> int:
        alpha="zyxwvutsrqponmlkjihgfedcba"
        res=0
        for i in range(len(s)):
            rank=alpha.index(s[i])+1
            res+=rank*(i+1)
        return res