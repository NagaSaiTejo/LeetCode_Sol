class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        ans = 0
        for i in range(len(nums) // 2):
            ans = max(ans, nums[i] + nums[-1 - i])
        return ans