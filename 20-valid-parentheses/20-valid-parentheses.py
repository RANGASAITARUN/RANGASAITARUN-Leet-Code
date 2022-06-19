class Solution:
    def isValid(self, s: str) -> bool:
        closed = {'}': '{', ']': '[', ')': '('}
        stack = []
        for c in s:
            if c not in closed:
                stack.append(c)
            else:
                if not stack or stack[-1] != closed[c]:
                    return False
                else:
                    stack.pop()
        return not stack
       
    