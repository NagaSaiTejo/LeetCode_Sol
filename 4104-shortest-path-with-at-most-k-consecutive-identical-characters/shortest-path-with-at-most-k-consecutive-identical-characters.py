import heapq 
from typing import List 

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj=[[] for i in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
        dist=[[float('inf')]*(k+1) for i in range(n)]
        dist[0][1]=0 
        pq=[(0,0,1)]
        while pq:
            d,u,c=heapq.heappop(pq)
            if d>dist[u][c]:
                continue 
            if u==n-1:
                return d 
            for v,w in adj[u]:
                nc=c+1 if labels[u]==labels[v] else 1 
                if nc<=k and d+w<dist[v][nc]:
                    dist[v][nc]=d+w 
                    heapq.heappush(pq,(d+w,v,nc))
        return -1