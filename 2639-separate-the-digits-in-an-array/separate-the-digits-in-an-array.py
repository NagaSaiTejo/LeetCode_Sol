class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans=[]
        for x in nums:
            for c in str(x):
                ans.append(int(c))
        return ans