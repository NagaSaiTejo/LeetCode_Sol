class Solution:
    def gen(self, n: str) -> str:
        ch=n[0]
        cnt=1
        s=""
        for i in range(1,len(n)):
            if ch==n[i]:
                cnt+=1
            else:
                s+=(str(cnt))+ch
                ch=n[i]
                cnt=1
        s+=str(cnt)+ch
        return s

    def countAndSay(self, n: int) -> str:
        if(n==1):
            return "1"
        s="1"    
        for i in range(2,n+1):
            s=self.gen(s)
        return s    
       