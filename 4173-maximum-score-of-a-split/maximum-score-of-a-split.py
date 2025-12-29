class Solution(object):
    def maximumScore(self, nums):
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        suffix[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = min(suffix[i+1], nums[i])
        ans = -10**18
        for i in range(n-1):
            v = prefix[i] - suffix[i+1]
            if v > ans:
                ans = v
        return ans