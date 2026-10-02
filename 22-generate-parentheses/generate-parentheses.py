class Solution:
    def generateParenthesis(self,n:int)->list[str]:
        res=[]
        def isValid(s):
            bal=0
            for c in s:
                if c=='(':
                    bal+=1
                else:
                    bal-=1
                if bal<0:
                    return False
            return bal==0
        def dfs(curr):
            if len(curr)==2*n:
                if isValid(curr):
                    res.append(curr)
                return
            dfs(curr+'(')
            dfs(curr+')')
        dfs('')
        return res