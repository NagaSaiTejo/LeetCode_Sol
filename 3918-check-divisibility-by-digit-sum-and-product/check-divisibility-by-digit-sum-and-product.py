class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        temp=n
        while temp>0:
            d=temp%10
            s+=d
            p*=d
            temp//=10
        return n%(s+p)==0
