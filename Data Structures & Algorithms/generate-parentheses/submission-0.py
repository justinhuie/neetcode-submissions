class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            # Check if we used all open and closed
            if openN == n and closedN == n:
                res.append("".join(stack))
            
            # If we can still append open append
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                # We pop to change branches
                stack.pop()
            
            # If we can close an open parenthesis we should close
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                # We pop to change branches
                stack.pop()
        
        backtrack(0, 0)
        return res
        