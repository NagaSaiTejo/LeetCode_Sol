class Solution(object):
    def totalWaviness(self, num1, num2):
        ans=0
        for i in range(num1,num2+1):
            s=str(i)
            si=len(s)
            c=0
            for j in range(1,si-1):
                cur=int(s[j])
                prevcur=int(s[j-1])
                postcur=int(s[j+1])
                if (cur>prevcur and cur>postcur) or (cur<prevcur and cur<postcur):
                    c+=1
            ans+=c
        return ans