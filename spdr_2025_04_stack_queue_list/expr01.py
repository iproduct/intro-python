
ops = {'+', '-'}

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
    else:
        raise Exception('Invalid operator')

def clculate(tokens: list[str]) -> int:
    operands = []
    operators = []
    for token in tokens:
        if token in ops:
           operators.append(token)
        else:
            operands.append(token)

    print(operators)
    print(operands)
    while operators:
        op = operators.pop(0)
        operand1 = operands.pop(0)
        operand2 = operands.pop(0)
        result = apply(op, operand1, operand2)
        print(op, operand1, operand2, result)
        operands.insert(0, result)
    return operands.pop()

def eval(expr: str) -> int:
    return clculate(tokenize(expr))


if __name__ == '__main__':
    print(eval('1+2'))
    print(eval('-12+23-5+ 16'))

