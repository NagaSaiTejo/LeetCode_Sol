class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        i=0 
        while i<n and s[i]==' ':
            i+=1 
        if i==n:
            return 0 
        sign=1 
        if s[i]=='-':
            sign=-1 
            i+=1 
        elif s[i]=='+':
            i+=1 
        res=0 
        MIN_INT=-2**31 
        MAX_INT=2**31-1 
        while i<n and '0'<=s[i]<='9':
            digit=ord(s[i])-ord('0')
            res=res*10+digit 
            i+=1 
        res*=sign 
        if res<MIN_INT:
            return MIN_INT 
        if res>MAX_INT:
            return MAX_INT 
        return res 