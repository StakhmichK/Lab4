a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if not (1 <= a <= 10 and 1 <= b <= 10 and \
 1 <= c <= 10 and 1 <= d <= 10):
    print("Error: numbers must be \
 between 1 and 10")
elif a > b or c > d:
    print("Error: a must be <= b and \
 c must be <= d")
else:
    print("\t", end="")
for j in range(c, d + 1):
    print(j, end="\t")
print()

for i in range(a, b + 1):
    print(i, end="\t")  
    for j in range(c, d + 1):
        print(i * j, end="\t")
    print()