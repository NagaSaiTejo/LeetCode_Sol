class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn=min(nums)
        mx=max(nums)
        res=[]
        for i in range(mn,mx+1):
            found=False
            for x in nums:
                if x==i:
                    found=True
                    break
            if not found:
                res.append(i)
        return res