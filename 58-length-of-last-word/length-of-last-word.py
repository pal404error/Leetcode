class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s[::-1]
        u = x.split()

        return len(u[0])