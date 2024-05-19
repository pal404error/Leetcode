class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r= 0, len(height) -1
        ans =0
        while l<r:
            m = min(height[l], height[r])
            t = m * (r-l)
            print(t)
            ans = max(t,ans)
            if(height[r] > height[l]):
                l+=1
            else:
                r-=1

        return ans