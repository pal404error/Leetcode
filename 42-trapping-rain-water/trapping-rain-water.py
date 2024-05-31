class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : return 0
        
        l, r = 0 , len(height)-1
        ml , mr = height[l], height[r]
        ans=0
        while l<r:
            if ml < mr:
                l+=1
                ml = max(height[l], ml)
                ans += ml - height[l]
            else:
                r-=1
                mr = max(height[r], mr)
                ans += mr - height[r]
                
        return ans