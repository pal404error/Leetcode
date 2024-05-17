class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(cha for cha in s if cha.isalnum())
        n = len(clean)
        c = clean.lower()
        print(clean)
        return c == c[::-1]