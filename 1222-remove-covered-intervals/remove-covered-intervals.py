class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ans=0 
        max_r=-1 
        for l,r in intervals:
            if r>max_r:
                ans+=1 
                max_r=r 
        return ans