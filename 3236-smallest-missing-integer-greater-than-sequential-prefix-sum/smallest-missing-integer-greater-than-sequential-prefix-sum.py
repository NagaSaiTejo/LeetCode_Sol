class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = 0
        for i,num in enumerate(nums):
            if i>0 and num!=nums[i-1]+1:
                break
            prefix_sum+=num
        while prefix_sum in nums:
            prefix_sum+=1
        return prefix_sum