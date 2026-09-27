class Solution:
    def reverseParentheses(self, s: str) -> str:
        n=len(s)
        st=[]
        pair=[0]*n
        for i in range(n):
            if s[i]=='(':
                st.append(i)
            elif s[i]==')':
                j=st.pop()
                pair[i]=j
                pair[j]=i
        res=[]
        i=0
        d=1
        while i<n:
            if s[i]=='(' or s[i]==')':
                i=pair[i]
                d=-d
            else:
                res.append(s[i])
            i+=d
        return "".join(res)