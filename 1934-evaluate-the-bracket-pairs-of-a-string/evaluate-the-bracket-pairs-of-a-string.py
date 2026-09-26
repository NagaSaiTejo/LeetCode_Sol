class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d=dict(knowledge)
        res=[]
        buf=[]
        inside=False
        for char in s:
            if char=='(':
                inside=True
                buf=[]
            elif char==')':
                inside=False
                k=''.join(buf)
                res.append(d.get(k,'?'))
            elif inside:
                buf.append(char)
            else:
                res.append(char)
        return ''.join(res)