class Solution(object):
    def maxSubArray(self, nums):
        ans = float('-inf')
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if ans<sum:
                ans=sum
            if sum<0:
                sum=0
        return ans