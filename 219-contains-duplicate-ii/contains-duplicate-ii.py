class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()

        for i in range(len(nums)):
            if i>k :
                win.remove(nums[i-k-1])
            if nums[i] in win:
                return True
            win.add(nums[i])

        return False