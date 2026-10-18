class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def solve(arr):
            if len(arr)<=2:
                return 1 
            l=[x for x in arr if x<arr[0]]
            r=[x for x in arr if x>arr[0]]
            return __import__('math').comb(len(l)+len(r),len(l))*solve(l)*solve(r)
        return (solve(nums)-1)%(10**9+7)