class Solution:
    def minInsertions(self, s: str) -> int:
        ans=0 
        rights=0 
        for c in s:
            if c=='(':
                if rights%2!=0:
                    ans+=1 
                    rights-=1 
                rights+=2 
            else:
                rights-=1 
                if rights<0:
                    ans+=1 
                    rights+=2 
        return ans+rights