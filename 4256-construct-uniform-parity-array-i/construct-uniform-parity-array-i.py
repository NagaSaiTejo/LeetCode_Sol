class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even=False
        odd=False
        for x in nums1:
            if x%2==0:
                even=True
            else: 
                odd=True
        return True