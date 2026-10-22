from collections import deque
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        is_inc=True
        is_dec=True
        for i in range(1,n):
            if nums[i]!=(nums[0]+i)%n:
                is_inc=False
            if nums[i]!=(nums[0]-i+n)%n:
                is_dec=False
        if not is_inc and not is_dec:
            return -1
        if is_inc:
            target_type=0
            target_shift=(n-nums[0])%n
        else:
            target_type=1
            target_shift=(n-nums[-1])%n
        dist={}
        q=deque([(0,0)])
        dist[(0,0)]=0
        while q:
            t,s=q.popleft()
            d=dist[(t,s)]
            if t==target_type and s==target_shift:
                return d
            n1=(t,(s+1)%n)
            if n1 not in dist:
                dist[n1]=d+1
                q.append(n1)
            n2=(1-t,(n-s)%n)
            if n2 not in dist:
                dist[n2]=d+1
                q.append(n2)
        return -1