class Solution(object):
    def pivotArray(self, nums, pivot):
        arr=[0]*len(nums)
        i=left=0
        j=right=len(nums)-1
        while i<len(nums) and j>=0:
            if nums[i]<pivot:
                arr[left]=nums[i]
                left+=1
            if nums[j]>pivot:
                arr[right]=nums[j]
                right-=1
            i+=1
            j-=1
        while left<=right:
            arr[left]=pivot
            left+=1
        return arr