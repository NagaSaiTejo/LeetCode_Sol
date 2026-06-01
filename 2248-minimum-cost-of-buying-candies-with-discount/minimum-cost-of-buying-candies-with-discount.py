class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        total = 0
        for i, c in enumerate(cost):
            if i % 3 != 2:
                total += c
        return total