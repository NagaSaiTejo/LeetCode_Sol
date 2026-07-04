class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)
        i=l-1
        while i>=0:
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
            i-=1
        return [1]+digits