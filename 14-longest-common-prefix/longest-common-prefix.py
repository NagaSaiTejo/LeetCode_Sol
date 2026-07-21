class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = "" 
        if not strs: 
            return st
        strs=sorted(strs)
        for i,j in zip(strs[0],strs[-1]):
            if i!=j:
                break
            st+=i
        return st