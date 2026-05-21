class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ss in s:
            if ss == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif ss == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            elif ss == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(ss)

        return len(stack) == 0