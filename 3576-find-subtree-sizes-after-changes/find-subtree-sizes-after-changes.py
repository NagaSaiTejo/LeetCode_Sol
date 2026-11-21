import sys 
sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n=len(parent)
        adj=[[] for i in range(n)]
        for i in range(1,n):
            adj[parent[i]].append(i)
        new_parent=[-1]*n 
        anc=[[] for i in range(26)]
        def dfs1(u):
            c=ord(s[u])-97 
            if anc[c]:
                new_parent[u]=anc[c][-1]
            else:
                new_parent[u]=parent[u]
            anc[c].append(u)
            for v in adj[u]:
                dfs1(v)
            anc[c].pop()
        dfs1(0)
        new_adj=[[] for i in range(n)]
        for i in range(1,n):
            new_adj[new_parent[i]].append(i)
        ans=[0]*n 
        def dfs2(u):
            size=1 
            for v in new_adj[u]:
                size+=dfs2(v)
            ans[u]=size 
            return size 
        dfs2(0)
        return ans