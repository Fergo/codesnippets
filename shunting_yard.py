tokens = {
    "-": 1,
    "+": 1,
    "*": 2,
    "/": 2,
    "^": 3,
    ")": 0,
    "(": 0
}

signs = {
    '+': "p",
    '-': "n"
}

operators = []
output = []
solve = []

text = input("Expression: ")

# use regex to split tokens
#expr = re.split('([^0-9.])', text)

# no-regex token splitting (no lib)
expr = []
number = ""
for char in ''.join(text.split()):
    if char in tokens:
        if number != "":
            expr.append(number)
        expr.append(char)
        number = ""
    else:
        number += char

if number != "":
    expr.append(number)

last_token = ""
# tokenizer
for token in expr:
    if token in tokens and token not in [')', '(']:
        # if there's a higher precedence operation in the stack, pop it to the output stack
        while (len(operators) > 0) and (tokens[operators[-1]] >= tokens[token]):
            output.append(operators.pop())

        # check if the operator is an "math computation" or a sign operator
        # if it's the latter, replace the +/- sign with p/m, to make things easier when solving
        if token in signs and last_token in signs:
            operators.append(signs[token])
        else:
            operators.append(token)
    elif token == '(': 
        operators.append(token)
    elif token == ')':
        # if we find a close bracket token, drain the operator stack until we find the close bracket token
        # brackets matching check is done later
        movimentar = operators.pop()
        while movimentar != '(':
            output.append(movimentar)
            if len(operators) > 0:
                movimentar = operators.pop()
    else:
        # if is not a token, must be a number or an invalid character
        try:
            output.append(float(token))
        except:
            print(f'ERROR: Undefined token: {token}')
            exit()

    last_token = token

while len(operators) > 0:
    output.append(operators.pop())

# check for bracket mismatch
if '(' in operators or ')' in operators:
    print(f'ERROR: Bracket mismatch')
    exit()

print(f"RPN: {' '.join(str(x) for x in output)}")

#solver
for token in output:
    # if number, directly add to the solve stack
    if isinstance(token, float):
        solve.append(token)
    # if it's a math operation
    elif token in tokens or token:
        if len(solve) < 2:
            print('ERROR: Not enough arguments or argument mismatch')
        else:
            arg0 = float(solve.pop())
            arg1 = float(solve.pop())

            result = 0
            if (token == '/'): result = arg1 / arg0
            elif (token == '*'): result = arg1 * arg0
            elif (token == '+'): result = arg1 + arg0
            elif (token == '-'): result = arg1 - arg0
            elif (token == '^'): result = arg1 ** arg0

            solve.append(result)
    # if it's a sign operation
    elif token in signs.values():
        if len(solve) < 1:
            print('ERROR: Not enough arguments or argument mismatch')
        else:
            arg0 = float(solve.pop())

            result = 0
            if (token == 'p'): result = arg0
            elif (token == 'n'): result = -arg0

            solve.append(result)

print(f"Result: {solve[0]}")
