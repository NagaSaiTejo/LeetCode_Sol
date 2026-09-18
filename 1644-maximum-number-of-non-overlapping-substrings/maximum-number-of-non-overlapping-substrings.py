class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first={c:i for i,c in reversed(list(enumerate(s)))}
        last={c:i for i,c in enumerate(s)}
        intervals=[]
        for c in set(s):
            l=first[c]
            r=last[c]
            valid=True
            i=l
            while i<=r:
                if first[s[i]]<l:
                    valid=False
                    break
                r=max(r,last[s[i]])
                i+=1
            if valid:
                intervals.append((l,r))
        intervals.sort(key=lambda x:x[1])
        ans=[]
        prev_end=-1
        for l,r in intervals:
            if l>prev_end:
                ans.append(s[l:r+1])
                prev_end=r
        return ans