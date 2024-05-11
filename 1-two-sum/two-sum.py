class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind ={}
        for n in range(len(nums)):
            sum = target - nums[n]
            
            if(sum in ind):
                return [ ind[sum], n]
            ind[nums[n]] = n
        return []