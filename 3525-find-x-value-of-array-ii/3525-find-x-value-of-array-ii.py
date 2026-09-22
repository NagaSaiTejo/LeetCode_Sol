class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        ans=[]
        for idx,val,start,x in queries:
            nums[idx]=val
            cnt=0
            prod=1
            for j in range(start,len(nums)):
                prod=(prod*nums[j])%k
                if prod==x:
                    cnt+=1
            ans.append(cnt)
        return ans