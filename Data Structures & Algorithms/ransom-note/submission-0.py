class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for s in magazine:
            key = ord(s)
            hashmap[key] = 1 + hashmap.get(key, 0)
        for s in ransomNote:
            letter = ord(s)
            if hashmap.get(letter, 0) > 0:
                hashmap[letter] -= 1
            else:
                return False
        return True
        