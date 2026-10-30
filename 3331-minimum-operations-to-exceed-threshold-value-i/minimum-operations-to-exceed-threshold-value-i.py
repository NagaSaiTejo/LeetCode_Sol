class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans=0 
        for x in nums:
            if x<k:
                ans+=1 
        return ans