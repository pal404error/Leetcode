class Solution:
    def x(self,p,mid) :
        time =0
        for j in p:
            time += ceil(j /mid)

        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)
        l=1
        while l<=n:
            mid = l +(n-l )// 2
            time= self.x(piles, mid)
            if time > h:
                l = mid+1
            else:
                n = mid-1

        return int(l)
