class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n
        for e in roads:
            deg[e[0]] += 1
            deg[e[1]] += 1
        
        deg.sort()
        ans = 0
        for i in range(n):
            ans += (i + 1) * deg[i]
        
        return ans    