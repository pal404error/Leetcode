class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        post =1
        for i in reversed(range(len(nums))):
            ans[i] = ans[i] * post
            post *= nums[i]
        
        return ans
        