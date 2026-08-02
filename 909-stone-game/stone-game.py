class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        evensum=sum(piles[i] for i in range(0,len(piles),2))
        oddsum=sum(piles[i] for i in range(1,len(piles),2))
        return evensum!=oddsum