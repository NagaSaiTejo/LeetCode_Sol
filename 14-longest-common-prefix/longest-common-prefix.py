class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs=sorted(strs)
        fw=strs[0]
        lw=strs[-1]
        res = ""
        for i in range(min(len(fw),len(lw))):
            if fw[i]==lw[i]:
                res+=fw[i]
            else:
                break
        return res