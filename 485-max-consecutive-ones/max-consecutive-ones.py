class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons=0
        a=0
        for i in nums:
            if i ==1:
                cons+=1
            else:
                cons=0
            a = max(a,cons)
            print(cons)
        return a