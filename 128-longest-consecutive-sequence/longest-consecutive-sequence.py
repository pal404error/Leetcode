class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        len = 0
        for n in nums:
            
            if n-1 not in numset:
                
                l =0
                while n+l in numset:
                    l +=1
                len = max(l,len)
        
        return len
               