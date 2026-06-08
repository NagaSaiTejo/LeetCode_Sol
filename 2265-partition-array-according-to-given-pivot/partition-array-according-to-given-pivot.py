class Solution(object):
    def pivotArray(self, nums, pivot):
        l=[]
        r=[]
        c=0
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i>pivot:
                r.append(i)
            else:
                c+=1
        r=l+ [pivot]*c +r
        return r
        # arr=[0]*len(nums)
        # i=0
        # left=0
        # j=len(nums)-1
        # right=len(nums)-1
        # while i<len(nums) and j>=0:
        #     if nums[i]<pivot:
        #         arr[left]=nums[i]
        #         left+=1
        #     if nums[j]>pivot:
        #         arr[right]=nums[j]
        #         right-=1
        #     i+=1
        #     j-=1
        # while left<=right:
        #     arr[left]=pivot
        #     left+=1
        # return arr