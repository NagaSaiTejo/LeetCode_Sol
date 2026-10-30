class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        n=len(nums)
        ans=1 
        curr=1 
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                curr+=1 
            else:
                curr=1 
            if curr>ans:
                ans=curr 
        return ans