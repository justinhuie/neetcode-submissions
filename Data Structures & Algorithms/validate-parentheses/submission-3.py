class Solution:
    def isValid(self, s: str) -> bool:
        # ([{}]) is valid
        # Notice how its always open and then close
        # We can use a stack to check validity

        stack = []
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}

        # for character in s
        # if character is in closeToOpen --> check top of stack to see if it matches
        # if so pop if not return false 
        # else append character to the stack

        # return true if stack is empty

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



     