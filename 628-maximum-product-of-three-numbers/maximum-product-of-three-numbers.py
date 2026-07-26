class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        p1=nums[-1]*nums[-2]*nums[-3]
        p2=nums[0]*nums[1]*nums[-1]
        if p1>p2:
            return p1
        return p2