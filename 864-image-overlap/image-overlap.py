class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        extended=[[0]*(3*n) for i in range(3*n)]
        for r in range(n):
            for c in range(n):
                extended[r+n][c+n]=img2[r][c]
        ans=0
        for rShift in range(2*n+1):
            for cShift in range(2*n+1):
                cnt=0
                for r in range(n):
                    for c in range(n):
                        if img1[r][c]==1 and extended[r+rShift][c+cShift]==1:
                            cnt+=1
                ans=max(ans,cnt)
        return ans