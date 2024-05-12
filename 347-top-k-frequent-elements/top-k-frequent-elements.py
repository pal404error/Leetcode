class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        c = Counter(nums)
        ans = [w for w, wo in c.most_common(k)]
        return ans
