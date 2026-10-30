class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0 
        for i in range(len(nums)):
            if nums[i]%3!=0:
                ans+=1 
        return ans