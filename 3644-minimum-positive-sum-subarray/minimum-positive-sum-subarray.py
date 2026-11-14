from bisect import bisect_left
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+nums[i]
        vals=sorted(set(pref))
        m=len(vals)
        bit=[0]*(m+1)
        def add(idx,val):
            while idx<=m:
                bit[idx]+=val
                idx+=idx&-idx
        def query(idx):
            s=0
            while idx>0:
                s+=bit[idx]
                idx-=idx&-idx
            return s
        def find_kth(k):
            idx=0
            bit_mask=1<<(m.bit_length()-1)
            while bit_mask>0:
                nxt=idx+bit_mask
                if nxt<=m and bit[nxt]<k:
                    k-=bit[nxt]
                    idx=nxt
                bit_mask>>=1
            return idx+1
        ans=float('inf')
        for j in range(l,n+1):
            add_idx=bisect_left(vals,pref[j-l])+1
            add(add_idx,1)
            if j-r-1>=0:
                rem_idx=bisect_left(vals,pref[j-r-1])+1
                add(rem_idx,-1)
            cur_idx=bisect_left(vals,pref[j])+1
            cnt=query(cur_idx-1)
            if cnt>0:
                best_idx=find_kth(cnt)
                diff=pref[j]-vals[best_idx-1]
                if diff<ans:
                    ans=diff
        return -1 if ans==float('inf') else ans