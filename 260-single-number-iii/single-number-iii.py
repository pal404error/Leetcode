class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if i not in ans:
                ans.append(i)
            else:
                ans.remove(i)
        
        return ans