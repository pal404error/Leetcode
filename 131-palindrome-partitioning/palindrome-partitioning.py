class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(s):
            return s == s[::-1]
        
        def back(start,a):
            if start == len(s):
                result.append(a[:])
                return
            for end in range(start+1, len(s)+1):
                if is_pal(s[start:end]):
                    back(end, a+[s[start:end]])

        result = []
        back(0,[])
        return result