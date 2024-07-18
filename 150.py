tokens=["3","11","5","+","-"]

stack = []
operators = "+-*/"
result = 0


if len(tokens) == 1:
    print(tokens[0])

def operation(n1, n2):
    if tokens[n] == "+":
        return n1 + n2
    if tokens[n] == "-":
        return n1 - n2
    if tokens[n] == "*":
        return n1 * n2
    if tokens[n] == "/":
        return int(n1 / n2)

for n in range(len(tokens)):
    if tokens[n] not in operators:
        stack.append(tokens[n])
    else:
        num1 = int(stack.pop())
        num2 = int(stack.pop())

        result = operation(num2, num1)

        stack.append(result)

        
print(result)