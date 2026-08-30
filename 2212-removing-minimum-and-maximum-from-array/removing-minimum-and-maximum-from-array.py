class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        mi=nums.index(min(nums))
        mx=nums.index(max(nums))
        a=min(mi,mx)
        b=max(mi,mx)
        opt1=b+1
        opt2=n-a
        opt3=(a+1)+(n-b)
        return min(opt1,opt2,opt3)