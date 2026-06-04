from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        freqs=Counter(arr)
        f=list(freqs.values())
        s=set(f)
        if len(f)==len(s):
            return True
        else:
            return False