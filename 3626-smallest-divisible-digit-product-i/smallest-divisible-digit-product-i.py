class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        x=n
        while True:
            p=1
            temp=x
            while temp>0:
                p*=temp%10
                temp//=10
            if p%t==0:
                print(x)
                break
            x+=1
        return x