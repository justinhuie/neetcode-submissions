class Solution:
    def isValid(self, s: str) -> bool:
        # Declare stack and hashmap to map close to open

        stack = []
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}

        # for each value in the the string
        # if its a open bracket we want to append to the stack
        # if its a closed bracket check if the closed bracket is same as the open bracket on top of the stack
        # if true --> pop from the stack (pair) else return false
        # if the array is empty then return true else false 

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False



     