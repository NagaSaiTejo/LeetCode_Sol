class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)<1:
            return ""
        start=0
        end=0
        for i in range(len(s)):
            l1,r1=i,i
            while l1>=0 and r1<len(s) and s[l1]==s[r1]:
                l1-=1
                r1+=1
            len1=r1-l1-1
            l2,r2=i,i+1
            while l2>=0 and r2<len(s) and s[l2]==s[r2]:
                l2-=1
                r2+=1
            len2=r2-l2-1
            m=max(len1,len2)
            if m>end-start:
                start=i-(m-1)//2
                end=i+m//2
        return s[start:end+1]