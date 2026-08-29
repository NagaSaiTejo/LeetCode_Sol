class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n=len(nums)
        pairs=sorted([(nums[i],i) for i in range(n)])
        ans=[0]*n
        i=0
        while i<n:
            j=i
            while j+1<n and pairs[j+1][0]-pairs[j][0]<=limit:
                j+=1
            indices=sorted([pairs[k][1] for k in range(i,j+1)])
            for k in range(len(indices)):
                ans[indices[k]]=pairs[i+k][0]
            i=j+1
        return ans