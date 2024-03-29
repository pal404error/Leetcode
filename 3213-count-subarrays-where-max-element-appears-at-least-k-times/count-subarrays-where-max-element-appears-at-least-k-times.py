class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans =0
        m = max(nums)
        coun =0
        l=0
        for n in range(len(nums)):
            if nums[n] == m:coun+=1
            while coun >= k:
                if nums[l] == m : coun-=1
                l+=1
            ans+=l
        return ans 
