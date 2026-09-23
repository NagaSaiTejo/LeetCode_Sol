class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        if target<0:
            return -1
        if target==0:
            return len(nums)
        left=0
        curr=0
        ans=-1
        for right in range(len(nums)):
            curr+=nums[right]
            while curr>target and left<=right:
                curr-=nums[left]
                left+=1
            if curr==target:
                ans=max(ans,right-left+1)
        return len(nums)-ans if ans!=-1 else -1