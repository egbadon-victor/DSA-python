class Solution:
    def doOperation(self, a:int, b:int,operator: str) -> int:
        match operator:
            case "+":
                return a + b
            case "-":
                return a-b
            case "*":
                return a*b
            case "/":
                return int(a/b)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        operands = []

        for t in tokens:
            if t in operators:
                b = int(operands.pop())
                a = int(operands.pop())
                operands.append(self.doOperation(a,b,t))
            else:
                operands.append(int(t))

        return operands.pop()



        