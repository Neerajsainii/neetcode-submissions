class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  =[]
        for i in tokens:
            if i == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == '-':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b) - int(a))
            elif i == '*':
                stack.append(int(stack.pop())*int(stack.pop()))
            elif i == '/':
                a,b = int(stack.pop()),int(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(i)
            print('stack',stack)
        return int(stack[0])

        