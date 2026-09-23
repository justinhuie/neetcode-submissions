class Solution:
    def hammingWeight(self, n: int) -> int:
        output = []
        res = 0
        while n > 0:

            if n % 2 == 1:
                n = math.floor(n / 2)
                output.append(1)
            if n % 2 == 0:
                n = math.floor(n / 2)
                output.append(0)
        
        for i in range(len(output)):
            if output[i] == 1:
                res += 1
        
        return res
        
        

        