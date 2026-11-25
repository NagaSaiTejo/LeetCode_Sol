class Solution:
    def smallestUniqueSubarray(self,nums:list[int])->int:
        n=len(nums)
        MOD1=10**9+7
        MOD2=10**9+9
        BASE1=100003
        BASE2=100019
        low=1
        high=n
        ans=n
        def check(length):
            if length>n:
                return False
            h1,h2=0,0
            p1,p2=1,1
            for i in range(length):
                h1=(h1*BASE1+nums[i])%MOD1
                h2=(h2*BASE2+nums[i])%MOD2
                if i>0:
                    p1=(p1*BASE1)%MOD1
                    p2=(p2*BASE2)%MOD2
            seen={(h1,h2):1}
            first_idx={(h1,h2):0}
            for i in range(length,n):
                h1=(h1-nums[i-length]*p1)%MOD1
                h1=(h1*BASE1+nums[i])%MOD1
                h2=(h2-nums[i-length]*p2)%MOD2
                h2=(h2*BASE2+nums[i])%MOD2
                pair=(h1,h2)
                seen[pair]=seen.get(pair,0)+1
            for cnt in seen.values():
                if cnt==1:
                    return True
            return False
        while low<=high:
            mid=(low+high)//2
            if check(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans