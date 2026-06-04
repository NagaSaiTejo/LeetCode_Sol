class Solution(object):
    def totalWaviness(self, num1, num2):
        ans=0
        for i in range(num1,num2+1):
            s=str(i)
            si=len(s)
            c=0
            for j in range(1,si-1):
                
                if (int(s[j])>int(s[j-1]) and int(s[j])>int(s[j+1])) or (int(s[j])<int(s[j-1]) and int(s[j])<int(s[j+1])):
                    c+=1
            ans+=c
        return ans