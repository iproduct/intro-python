
ops = {'+': ( 10, 'l'), '-': ( 10, 'l'), '*': ( 20, 'l'), '/': ( 20, 'l'),}

def is_op1_higer_precedence(op1: str, op2: str) -> bool:
    op1_data, op2_data = ops[op1], ops[op2]
    if op1_data[0] > op2_data[0]:
        return True
    elif op1_data[0] < op2_data[0]:
        return False
    else:
        if op2_data[1] == 'l':
            return True
        else:
            return False

def tokenize(expr: str) -> list[str]:
    expr = expr.replace(' ', '')
    accumulator = 0
    tokens = []
    for token in expr:
        if token in ops:
            tokens.append(accumulator)
            tokens.append(token)
            accumulator = 0
        else:
            accumulator = 10 * accumulator + int(token)
    tokens.append(accumulator)
    return tokens

def apply(operator: str, operand1: int, operand2: int) -> int:
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 // operand2
    else:
        raise Exception('Invalid operator')

def clculate(tokens: list[str]) -> int:
    def execute_op(operator: str) -> int:
        operand1 = operands.pop()
        operand2 = operands.pop()
        result = apply(operator, operand2, operand1)
        print(operator, operand2, operand1, result)
        operands.append(result)

    operands = []
    operators = []
    for token in tokens:
        if token in ops:
            while operators and is_op1_higer_precedence(operators[-1], token):
                prev_op = operators.pop()
                execute_op(prev_op)
            operators.append(token)
        else:
            operands.append(token)
    print(operators)
    print(operands)
    while operators:
        execute_op(operators.pop())
    return operands.pop()

def eval(expr: str) -> int:
    return clculate(tokenize(expr))


if __name__ == '__main__':
    print(eval('1+2'))
    print(eval('12 * 2 +2 -5 * 3+ 16'))

