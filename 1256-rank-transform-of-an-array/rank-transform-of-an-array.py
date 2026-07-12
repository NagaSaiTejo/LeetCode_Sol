class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: 
            return []
        sorted_unique=sorted(set(arr))
        rank_map={}
        i=1
        for v in sorted_unique:
            rank_map[v]=i
            i+=1
        return [rank_map[x] for x in arr]