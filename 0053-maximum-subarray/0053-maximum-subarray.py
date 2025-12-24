class Solution(object):
    def maxSubArray(self, nums):
        #ans = -math.inf
        # Or simply
        ans = -99999
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if ans<sum:
                ans=sum
            if sum<0:
                sum=0
        return ans