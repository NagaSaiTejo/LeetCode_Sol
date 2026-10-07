class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(strVal):
            cnt=0
            for char in strVal:
                if char=='(':
                    cnt+=1
                elif char==')':
                    cnt-=1
                    if cnt<0:
                        return False
            return cnt==0
        if not s:
            return [""]
        level={s}
        while True:
            valid=list(filter(isValid,level))
            if valid:
                return valid
            nextLevel=set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":
                        nextLevel.add(item[:i]+item[i+1:])
            level=nextLevel