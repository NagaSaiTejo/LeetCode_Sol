class Solution(object):
    def countVowelStrings(self, n):
        a=e=i=o=u=1
        n-=1
        while n:
            o+=u
            i+=o
            e+=i
            a+=e
            n-=1
        return a+e+i+o+u