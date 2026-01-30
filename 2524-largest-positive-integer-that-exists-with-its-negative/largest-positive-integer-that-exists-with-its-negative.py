class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s=set(nums)
        Max=-1
        for i in s:
            if (i*-1) in s:
                Max=max(Max,abs(i))
        return Max