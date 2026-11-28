class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f=max(f for f,p in items)
        cnt=[0]*(max_f+1)
        min_p=items[0][1]
        for f,p in items:
            cnt[f]+=1
            if p<min_p:
                min_p=p
        gain_by_f=[0]*(max_f+1)
        for f in range(1,max_f+1):
            if cnt[f]>0:
                total=-1
                for m in range(f,max_f+1,f):
                    total+=cnt[m]
                gain_by_f[f]=total
        limit=2*min_p
        candidates=[]
        for f,p in items:
            g=gain_by_f[f]
            if g>0 and p<limit:
                candidates.append((p,g))
        candidates.sort()
        ans=0
        rem=budget
        for p,g in candidates:
            take=min(g,rem//p)
            ans+=take*2
            rem-=take*p
            if take<g:
                break
        ans+=rem//min_p
        return ans