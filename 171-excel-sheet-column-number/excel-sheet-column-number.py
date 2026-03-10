class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r = 0
        for i in columnTitle:
            r=(r*26) + ord(i) -65 +1
        return r