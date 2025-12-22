class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        s=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if (j-i)%2==0:
                    for k in range(i,j+1):
                        s+=arr[k]
        return s