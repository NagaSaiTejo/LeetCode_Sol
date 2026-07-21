class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        n=len(nums)//2
        for i,cc in c.items():
            if cc>n:
                maxi=i
                break
        return maxi