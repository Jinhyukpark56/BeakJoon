A = int(input().strip())

operator = input().strip()

B = int(input().strip())

if operator == '+':
    result = A + B
elif operator == '*':
    result = A * B

print(result)