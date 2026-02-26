class Solution:
    def numSteps(self, s: str) -> int:
        ss=int(s,2)
        c=0
        while ss!=1:
            if ss % 2 != 0:
                ss=ss+1
                c+=1
            elif ss % 2 == 0:
                ss=ss//2
                c+=1
        return c