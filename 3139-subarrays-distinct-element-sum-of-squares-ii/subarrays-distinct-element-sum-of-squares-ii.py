class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        MOD=10**9+7
        last={}
        bit1=[0]*(n+2)
        bit2=[0]*(n+2)
        curr_sum_sq=0
        ans=0
        for i in range(n):
            x=nums[i]
            l=last.get(x,-1)+1
            r=i
            last[x]=i
            sum_d=0
            p=r+1
            while p>0:
                sum_d+=bit1[p]*(r+1)-bit2[p]
                p-=p&(-p)
            p=l
            while p>0:
                sum_d-=bit1[p]*l-bit2[p]
                p-=p&(-p)
            cnt=r-l+1
            curr_sum_sq=(curr_sum_sq+2*sum_d+cnt)%MOD
            ans=(ans+curr_sum_sq)%MOD
            for idx,val in [(l+1,1),(r+2,-1)]:
                p=idx
                while p<=n+1:
                    bit1[p]+=val
                    bit2[p]+=val*(idx-1)
                    p+=p&(-p)
        return ans