class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        mis=[]
        for nums in range(1, len(nums)+1):
            if nums not in s:
                mis.append(nums)
        
        return mis