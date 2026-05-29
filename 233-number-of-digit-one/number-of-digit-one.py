class Solution(object):
    def countDigitOne(self, n):
         return sum((n // (10**(p+1))) * (10**p) + ( (n % (10**p) + 1) if ((n // (10**p)) % 10 == 1) else ( (10**p) if ((n // (10**p)) % 10 > 1) else 0 ) ) for p in range(len(str(n))))