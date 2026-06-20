class Solution:
    def reverse(self, x: int) -> int:
        maxi=2**31-1
        mini=-2**31
        neg=x<0
        num=abs(x)
        res=0
        while num>0:
            digit=num%10
            res=res*10+digit
            num//=10
        if neg:
            res=-res
        if res>maxi or res<mini:
            return 0
        else:
            return res