class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor_all=0
        for num in nums:
            xor_all^=num
        if xor_all!=0:
            return len(nums)
        if all(num==0 for num in nums):
            return 0
        return len(nums)-1