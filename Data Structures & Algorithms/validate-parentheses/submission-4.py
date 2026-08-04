class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}": "{", "]" : "[", ")" : "("}

        # look through  string
        # if its an open bracket append to the stack
        # if its a closed bracket check if stack non empty and if stack[-1] top of stack is equal to the value associated with key
        # if so then we can pop
        # if not return false
        # if stack is empty return true else false

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False


     