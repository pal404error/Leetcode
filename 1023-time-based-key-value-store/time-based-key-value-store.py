class TimeMap:

    def __init__(self):
        self.s = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.s:
            self.s[key] = []
        self.s[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        v = self.s.get(key, [])
        l,r = 0,len(v)-1

        while l<=r:
            m = (r+l) // 2
            if v[m][1] <= timestamp:
                ans = v[m][0]
                l = m+1
            else:
                r = m-1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)