x = int(input("Enter first number\n"))
y = int(input("Enter second number\n"))

if x<y:
    small = x
    big = y
else:
    small = y
    big = x
for i in range(2,small+1):
    if (small % i ==0) and (big % i ==0):
            print(f"{i} is a multipler\n")
