class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
                continue
            print(stack)
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(int(left / right))

        return stack.pop()