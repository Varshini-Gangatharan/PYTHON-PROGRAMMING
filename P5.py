def calculate(s):
    stack = []
    current_number = 0
    current_operator = '+'
    for char in s + '+': 
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char in {'+', '-', '*', '/'}:
            if current_operator == '+':
                stack.append(current_number)
            elif current_operator == '-':
                stack.append(-current_number)
            elif current_operator == '*':
                stack[-1] *= current_number
            elif current_operator == '/':                
                stack[-1] = int(stack[-1] / current_number)
            current_number = 0
            current_operator = char
    return sum(stack)
s = "3+2*2"
result = calculate(s)
print(result)
