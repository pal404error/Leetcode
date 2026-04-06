class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mprice= prices[0]
        mprof = 0
        for i in prices[1:]:
            mprof = max(mprof, i-mprice)
            mprice = min(mprice, i)
        return mprof