class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts={}
        i=0
        ans=0
        for j in range(len(nums)):
            counts[nums[j]]=counts.get(nums[j],0)+1
            while counts[nums[j]]>k:
                counts[nums[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans