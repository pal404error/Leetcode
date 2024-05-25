class Solution:
    def isValid(self, s: str) -> bool:
        z = []
        temp = s
        for i in s:
            q = temp.replace("abc", '')
            temp = q
        if len(temp) != 0:
            return False

        return True

                