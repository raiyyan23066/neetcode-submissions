class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared=""
        for chars in s:
            if chars.isalnum():
                cleared+=chars.lower()
        return cleared==cleared[::-1]
        