class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=0 
        s=0 
        mul=1 
        while n>0:
            d=n%10 
            n//=10 
            if d!=0:
                x+=d*mul 
                mul*=10 
                s+=d 
        return x*s
        