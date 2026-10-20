class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        s=sorted(nums)
        divs=[]
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                divs.append(i)
                if i*i!=n:
                    divs.append(n//i)
        ans=0
        for k in divs:
            ok=True
            for i in range(0,n,k):
                b=nums[i:i+k]
                t=s[i:i+k]
                drops=[]
                for j in range(k-1):
                    if b[j]>b[j+1]:
                        drops.append(j)
                if len(drops)>1:
                    ok=False
                    break
                elif len(drops)==0:
                    if b!=t:
                        ok=False
                        break
                else:
                    idx=drops[0]+1
                    if b[idx:]+b[:idx]!=t:
                        ok=False
                        break
            if ok:
                ans+=k
        return ans