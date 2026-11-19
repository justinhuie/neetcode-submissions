class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        if not s:
            return True

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        l = 0
        r = len(newStr) - 1
        while l <= r:
            if newStr[l] != newStr[r]:
                return False
            r -= 1
            l += 1
        return True