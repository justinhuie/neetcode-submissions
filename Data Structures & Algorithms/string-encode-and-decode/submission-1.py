class Solution:

    def encode(self, strs: List[str]) -> str:
        # Set res to empty string and append length of string + delimiter + s
        res = ""
        for s in strs:
            res += (str(len(s)) + "#" + s)
        return res

    def decode(self, s: str) -> List[str]:
        # We want to have i as pointer and j as pointer to find #
        # Once we find # we set length to [i:j] which would be the length of str
        # Then we parse s by appending [j + 1: j + 1 + length] we need the +1 since end is exclusive
        # Then we set i = j + 1 + length since thats where we left off
        res = []
        i = 0
        while len(s) > i:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
       
