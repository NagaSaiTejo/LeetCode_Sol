class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans=0
        open_count=0
        for i in s:
            if i=='(':
                open_count+=1
            else:
                if open_count>0:
                    open_count-=1
                else:
                    ans+=1
        return ans+open_count