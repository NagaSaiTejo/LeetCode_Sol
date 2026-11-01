class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        ans=0 
        for i in range(1,len(nums)):
            ans+=nums[i]-nums[0]
        return ans 