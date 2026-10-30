class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s=set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                res.append(i)
        return res