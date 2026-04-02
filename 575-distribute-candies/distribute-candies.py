class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        typ = set(candyType)
        return min(len(candyType)//2, len(typ))