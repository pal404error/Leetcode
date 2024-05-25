class Solution:
    def isValid(self, s: str) -> bool:
        temp = s
        for i in s:
            if len(temp) == 0:
                return True
            q = temp.replace("abc", '')
            temp = q
        return False

                