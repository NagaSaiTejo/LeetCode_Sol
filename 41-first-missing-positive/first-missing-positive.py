class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        ans=1
        for i in range(n):
            if nums[i]>0 and nums[i]==ans:
                ans+=1
        return ans