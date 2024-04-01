class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        for i in s:
            a = s.split()

        print()

        c = len(a[-1])
        return c