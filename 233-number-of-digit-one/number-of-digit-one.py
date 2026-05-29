class Solution(object):
    def countDigitOne(self, n):
        total=0
        num_digits=len(str(n))
        for p in range(num_digits):
            power=10**p
            high=n//(power * 10)
            cur=(n // power) % 10
            low=n%power
            total+=high*power
            if cur==1:
                total+=low + 1
            elif cur>1:
                total+=power
        return total