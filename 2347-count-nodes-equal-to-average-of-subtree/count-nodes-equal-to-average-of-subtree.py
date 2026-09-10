# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans=0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0,0
            s1,c1=dfs(node.left)
            s2,c2=dfs(node.right)
            s,c=node.val+s1+s2,1+c1+c2
            if node.val==s//c:
                ans+=1
            return s,c
        dfs(root)
        return ans