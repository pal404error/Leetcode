class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, ans = len(grid), []

        for i in range(1,n-1):
            trow =[]
            for j in range(1, n-1):
                m =0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        m = max(m, grid[k][l])
                
                trow.append(m)
            ans.append(trow)
        return ans