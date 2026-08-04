class Solution:
    def isValid(self, s: str) -> bool:
        # Declare stack
        # Declare hashmap to map the closed brackets to the open ones

        # Loop through the string and if its open then append to the stack
        # if closed check top of stack to see if the closed bracket matches the open
        # if not, then its not a valid string if true, then we can pop
        # the string is valid iff the stack is empty by the end

        stack = []
        closeToOpen = {')' : '(', ']' : '[', '}' : '{'}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False



     