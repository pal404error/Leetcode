class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ct = [0] * (n+1)
        ct[0] = 1
        ans,t=0,0
        
        for a in nums:
            t+= a&1
            if t-k >=0:
                ans+=ct[t-k]
            ct[t]+=1
            
        return ans
        