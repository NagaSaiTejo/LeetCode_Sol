class Solution:
    def processStr(self, s: str) -> str:
        res=""
        for i in s:
            if 'a'<=i and 'z'>=i:
                res+=i
            elif i=='*':
                if res:
                    res=res[:-1]
            elif i=="#":
                res+=res
            elif i=='%':
                res=res[::-1]
        return res