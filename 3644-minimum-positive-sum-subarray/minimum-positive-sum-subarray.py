class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        ans=float('inf')
        for i in range(n):
            current_sum=0
            for j in range(i,n):
                current_sum+=nums[j]
                length=j-i+1
                if length>=l and length<=r and current_sum>0:
                    ans=min(ans,current_sum)
                if length>r:
                    break
        return ans if ans!=float('inf') else -1