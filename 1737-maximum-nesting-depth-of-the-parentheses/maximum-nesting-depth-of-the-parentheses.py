class Solution:
    def maxDepth(self, s: str) -> int:
        cur=0
        res=0
        for ch in s:
            if ch=='(':
                cur+=1
                if cur>res:
                    res=cur
            elif ch==')':
                cur-=1
        return res