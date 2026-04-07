class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mer = nums1 + nums2
        mer.sort()
        i = len(mer)
        if i%2 ==1:
            return float(mer[i // 2])
        else:
            m1 = mer[i // 2 - 1]
            m2 = mer[i // 2]
            return (float(m1)+ float(m2))/2.0
