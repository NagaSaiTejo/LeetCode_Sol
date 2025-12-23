class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        ts = 0
        for i in range(len(arr)):
            left=i+1
            right=len(arr)-i
            total=left*right
            odd_count=(total + 1)//2
            ts+=arr[i]*odd_count
        return ts