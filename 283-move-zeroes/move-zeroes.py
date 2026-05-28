class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        no, i=0,0
        while i< len(nums):
            if nums[i] != 0:
                nums[i], nums[no] = nums[no], nums[i]
                no += 1
            i +=1