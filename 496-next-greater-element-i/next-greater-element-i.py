class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            ng=-1
            found= False
            for j in nums2:
                if j == i:
                    found=True
                elif found:
                    if j > i:
                        ng = j
                        break
        
            res.append(ng)

        return res