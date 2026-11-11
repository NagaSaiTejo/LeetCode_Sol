class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        c1=min(cost1, costBoth)
        c2=min(cost2, costBoth)
        common=min(need1, need2)
        rem1=need1-common
        rem2=need2-common
        return common*min(costBoth, c1+c2)+rem1*c1+rem2*c2
