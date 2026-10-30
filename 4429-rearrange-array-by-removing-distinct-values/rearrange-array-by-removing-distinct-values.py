from collections import Counter 
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        counts=Counter(nums)
        items=[]
        for val,freq in counts.items():
            for round_idx in range(freq):
                items.append((round_idx,val))
        items.sort()
        return [val for round_idx,val in items]