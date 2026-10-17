class Solution:
    def minSwaps(self,nums:List[int])->int:
        target={v:i for i,v in enumerate(sorted(nums,key=lambda x:(sum(int(c) for c in str(x)),x)))}
        ans=0 
        for i in range(len(nums)):
            while target[nums[i]]!=i:
                j=target[nums[i]]
                nums[i],nums[j]=nums[j],nums[i]
                ans+=1 
        return ans