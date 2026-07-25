class Solution:
    def maxProduct(self, n: int) -> int:
        m1=0
        m2=0
        for i in str(n):
            v=int(i)
            if v>m1:
                m2=m1
                m1=v
            elif v>m2:
                m2=v
        return m1*m2