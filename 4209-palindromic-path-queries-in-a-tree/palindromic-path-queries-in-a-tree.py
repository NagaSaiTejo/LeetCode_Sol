import sys
sys.setrecursionlimit(200000)
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent=[-1]*n
        depth=[0]*n
        heavy=[-1]*n
        head=[0]*n
        pos=[0]*n
        size=[0]*n
        def dfs1(u,p,d):
            size[u]=1
            depth[u]=d
            parent[u]=p
            max_subtree=0
            for v in adj[u]:
                if v!=p:
                    dfs1(v,u,d+1)
                    size[u]+=size[v]
                    if size[v]>max_subtree:
                        max_subtree=size[v]
                        heavy[u]=v
        dfs1(0,-1,0)
        cur_pos=0
        def dfs2(u,h):
            nonlocal cur_pos
            head[u]=h
            pos[u]=cur_pos
            cur_pos+=1
            if heavy[u]!=-1:
                dfs2(heavy[u],h)
            for v in adj[u]:
                if v!=parent[u] and v!=heavy[u]:
                    dfs2(v,v)
        dfs2(0,0)
        tree=[0]*(4*n)
        chars=list(s)
        def update_tree(node,start,end,idx,val):
            if start==end:
                tree[node]=val
                return
            mid=(start+end)//2
            if start<=idx<=mid:
                update_tree(2*node,start,mid,idx,val)
            else:
                update_tree(2*node+1,mid+1,end,idx,val)
            tree[node]=tree[2*node]^tree[2*node+1]
        def query_tree(node,start,end,l,r):
            if r<start or end<l:
                return 0
            if l<=start and end<=r:
                return tree[node]
            mid=(start+end)//2
            return query_tree(2*node,start,mid,l,r)^query_tree(2*node+1,mid+1,end,l,r)
        for i in range(n):
            mask=1<<(ord(chars[i])-ord('a'))
            update_tree(1,0,n-1,pos[i],mask)
        def query_path(u,v):
            res=0
            while head[u]!=head[v]:
                if depth[head[u]]<depth[head[v]]:
                    u,v=v,u
                res^=query_tree(1,0,n-1,pos[head[u]],pos[u])
                u=parent[head[u]]
            if depth[u]>depth[v]:
                u,v=v,u
            res^=query_tree(1,0,n-1,pos[u],pos[v])
            return res
        ans=[]
        for q in queries:
            parts=q.split()
            if parts[0]=="update":
                ui=int(parts[1])
                c=parts[2]
                chars[ui]=c
                mask=1<<(ord(c)-ord('a'))
                update_tree(1,0,n-1,pos[ui],mask)
            else:
                ui,vi=int(parts[1]),int(parts[2])
                mask=query_path(ui,vi)
                if (mask&(mask-1))==0:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans