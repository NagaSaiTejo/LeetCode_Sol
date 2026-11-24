class Solution:
    def maxLength(self,nums:list[int])->int:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        def lcm(a,b):
            return(a*b)//gcd(a,b)
        n=len(nums)
        ans=1
        for i in range(n):
            curr_prod=nums[i]
            curr_gcd=nums[i]
            curr_lcm=nums[i]
            for j in range(i+1,n):
                curr_prod*=nums[j]
                curr_gcd=gcd(curr_gcd,nums[j])
                curr_lcm=lcm(curr_lcm,nums[j])
                if curr_prod==curr_lcm*curr_gcd:
                    ans=max(ans,j-i+1)
                elif curr_prod>curr_lcm*curr_gcd:
                    break
        return ans