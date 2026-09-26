class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        ans=0
        while l<r:
            h=min(height[l],height[r])
            cur=h*(r-l)
            if cur>ans:
                ans=cur
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans