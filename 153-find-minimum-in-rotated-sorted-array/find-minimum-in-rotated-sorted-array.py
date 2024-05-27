class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums)-1
        l =0
        while r>l:
            mid = (r+l)//2
            if int(nums[mid]) < int(nums[r]):
                r = mid
            else:
                l = mid+1
            

        return nums[l]