class Solution:
    def search(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            if target==nums[i]:
                return i
                c+=1
                break
        else:
            return -1