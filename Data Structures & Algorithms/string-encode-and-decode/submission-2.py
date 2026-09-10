class Solution:

    def encode(self, strs: List[str]) -> str:
        # Have # as delimiter and add str(len(s)) before appending s
        res = ""
        for s in strs:
            res += (str(len(s)) + "#" + s)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while len(s) > i:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            res.append(s[j + 1: j + 1 + length]) # 4#neet
            i = 1 + j + length
        return res


       
