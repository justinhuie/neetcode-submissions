class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while not self.alphaNum(s[l]):
                l += 1
                if l > len(s) - 1:
                    return True
            while not self.alphaNum(s[r]):
                r -= 1
                if r == 0:
                    return True
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))