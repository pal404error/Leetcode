class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        count=Counter(nums1)
        for n in nums2:
            if count[n]>0:
                ans.append(n)
            count[n]-=1
        return ans