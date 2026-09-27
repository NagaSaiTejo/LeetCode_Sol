class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        c=Counter(digits)
        return sum(1 for n in range(100,1000,2) if not(Counter(map(int,str(n)))-c))