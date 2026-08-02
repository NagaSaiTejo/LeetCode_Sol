class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        evensum=0
        oddsum=0
        n=len(piles)
        
        for i in range(n):
            if i%2==0:
                evensum=evensum+piles[i]
            else:
                oddsum=oddsum+piles[i]
                
        if evensum!=oddsum:
            return True
        else:
            return False