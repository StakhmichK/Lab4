a = int(input("Enter the start number: "))
n = int(input("Enter the end number: "))

total = 0
expression = ""

for i in range(a, n):
    term = f"{i}*{i+1}"
    expression += term
    if i != n - 1:
        expression += "+"
    total += i * (i + 1)
print(expression + "=" + str(total))