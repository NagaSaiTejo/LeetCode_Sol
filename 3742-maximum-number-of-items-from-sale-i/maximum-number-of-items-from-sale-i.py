class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        maxf=max(item[0] for item in items)
        cnt=[0]*(maxf+1)
        minp=items[0][1]
        for f,p in items:
            cnt[f]+=1 
            if p<minp:
                minp=p 
        div=[0]*(maxf+1)
        for f in range(1,maxf+1):
            if cnt[f]>0:
                total=0 
                for m in range(f,maxf+1,f):
                    total+=cnt[m]
                div[f]=total 
        dp=[0]*(budget+1)
        for f,p in items:
            if p>budget:
                continue 
            val=div[f]
            for w in range(budget,p-1,-1):
                cand=dp[w-p]+val 
                if cand>dp[w]:
                    dp[w]=cand 
        ans=0 
        for w in range(budget+1):
            cand=dp[w]+(budget-w)//minp
            if cand>ans:
                ans=cand 
        return ans