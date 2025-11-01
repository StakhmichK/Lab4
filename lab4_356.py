n = int(input("Enter the end number: "))

total = 0
expression = ""

for i in range(1, n):
    term = f"{i}*{i+1}"
    expression += term
    if i != n - 1:
        expression += "+"
    total += i * (i + 1)

print(expression + "=" + str(total))