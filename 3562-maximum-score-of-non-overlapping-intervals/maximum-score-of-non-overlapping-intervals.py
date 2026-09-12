class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        a=sorted((r,l,w,i) for i,(l,r,w) in enumerate(intervals))
        ends=[x[0] for x in a]
        memo={}
        def f(idx,c):
            if idx<0 or c==0:return 0,[]
            if (idx,c) in memo:return memo[(idx,c)]
            skip=f(idx-1,c)
            r,l,w,i=a[idx]
            p=bisect_left(ends,l)-1
            tw,ti=f(p,c-1)
            take=(w+tw,sorted(ti+[i]))
            memo[(idx,c)]=max(skip,take,key=lambda x:(x[0],[-j for j in x[1]]))
            return memo[(idx,c)]
        return f(len(a)-1,4)[1]