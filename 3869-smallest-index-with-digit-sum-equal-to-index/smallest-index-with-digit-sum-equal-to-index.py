class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,x in enumerate(nums):
            n,s=x,0
            while n>0:
                s+=n%10
                n//=10
            if s==i:
                return i
        return -1