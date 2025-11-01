expr = input("Enter your equation: ").strip()
result = int(expr[0])

for i in range(1, len(expr), 2):
     op = expr[i]
     num = int(expr[i+1])

     if op == '+':
        result += num
     else:
         result -= num
print("Your result is: ",result)