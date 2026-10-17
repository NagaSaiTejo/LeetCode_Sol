class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q,mx=[0],0 
        while q:
            i=q.pop(0)
            if i==len(s)-1:
                return True 
            for j in range(max(i+minJump,mx+1),min(i+maxJump+1,len(s))):
                if s[j]=='0':
                    q.append(j)
            mx=max(mx,i+maxJump)
        return False